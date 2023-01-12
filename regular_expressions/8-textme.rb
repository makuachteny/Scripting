#!/usr/bin/env ruby
log_line = ARGV[0]
sender = log_line[/from:(\S+)/, 1]
receiver = log_line[/to:(\S+)/, 1]
flags = log_line[/flags:(\S+)/, 1]

puts "#{sender},#{receiver},#{flags}"
