#!/usr/bin/pup
# Install Nginx web server (w/ Puppet)

package { 'nginx':
  ensure => installed,
}
file { '/var/www/html/index.html':
  content => 'Hello World!',
}
file_line { 'default':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}

file_line { 'add-header_X-Served-By':
  ensure      => 'present',
  path        => '/etc/nginx/sites-available/default',
  environment => ["HOST=${hostname}"],
  after       => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
  line        => "add_header X-Served-By ${HOST};",
}
service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
