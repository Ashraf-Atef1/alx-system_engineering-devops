#!/usr/bin/pup
package { 'python3-pip':
  ensure => installed,
}

exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  path    => ['/bin', '/usr/bin'],
  unless  => '/usr/bin/pip3 show Flask | grep -q "Version: 2.1.0"',
}

# Optional: Ensure flask is globally accessible
file { '/usr/local/bin/flask':
  ensure  => link,
  target  => '/usr/local/bin/flask',
  require => Exec['install_flask'],
}
