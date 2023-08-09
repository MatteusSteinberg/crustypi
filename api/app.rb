require 'sinatra'
require 'sinatra-websocket'

require 'mongoid'
require 'json'

Mongoid.load!(File.join(File.dirname(__FILE__), 'config', 'mongoid.yml'))

set :server, 'thin'
set :sockets, []

class Measures
  include Mongoid::Document

  field :temperature, type: Integer
  field :humidity, type: Integer
  field :pressure, type: Integer
  field :timestamp, type: Date

end

before do
  content_type :json

  request.body.rewind
  @request_payload = JSON.parse(request.body.read, symbolize_names: true)
end

get '/measures' do
  if params
    page = params[:page].to_i || 1
    per_page = params[:per_page].to_i || 10
    measures = Measures.skip((page - 1) * per_page).limit(per_page)
    total_pages = (Measures.count / per_page.to_f).ceil
    {
      measures: measures,
      page: page,
      per_page: per_page,
      total_pages: total_pages
    }.to_json
  else
    Measures.all.to_json
  end 
end

get '/' do
  if !request.websocket?
    erb :index
  else
    request.websocket do |ws|
      ws.onopen do
        ws.send("Hello World!")
        settings.sockets << ws
      end
      ws.onmessage do |msg|
        EM.next_tick { settings.sockets.each{|s| s.send(msg) } }
      end
      ws.onclose do
        warn("websocket closed")
        settings.sockets.delete(ws)
      end
    end
  end
end

post '/measures' do
  @request_payload.each do |data|
    Measures.create!(data)
  end
  status 201
end

get '/measures/:measure' do |measure|
  measures = Measures.find(measure)
  measures.to_json
end