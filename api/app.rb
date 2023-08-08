require 'sinatra'
require 'mongoid'
require 'json'

Mongoid.load!(File.join(File.dirname(__FILE__), 'config', 'mongoid.yml'))

class AirQuality
  include Mongoid::Document

  field :value, type: Integer
  field :type, type: String
  field :timestamp, type: Date

end

before do
  content_type :json

  request.body.rewind
  @request_payload = JSON.parse(request.body.read, symbolize_names: true)
end

get '/air-quality' do
  AirQuality.all.to_json
end

post '/air-quality' do
  @request_payload.each do |data|
    AirQuality.create!(data)
  end
  status 201
end

get '/air-quality/:fart' do |fart|
  air_quality = AirQuality.find(fart)
  air_quality.to_json
end