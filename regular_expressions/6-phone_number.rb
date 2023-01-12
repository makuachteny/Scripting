#!/usr/bin/env ruby
puts ARGV[0].scan(/\A(\d{3})[.-]?(\d{3})[.-]?(\d{4})\z/).join
