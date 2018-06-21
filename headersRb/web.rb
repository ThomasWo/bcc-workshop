require 'json'
require 'sinatra'
require 'uri'

get '/' do
  headers.to_json
end