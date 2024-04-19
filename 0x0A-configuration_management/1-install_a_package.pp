# Install an especific version of flask (2.1.0)

package { 'python3-pip':
  ensure => installed,
}

exec { 'install_flask':
  command     => '/usr/bin/pip3 install flask==2.1.0',
  path        => ['/bin', '/usr/bin'],
  environment => [],
  require     => Package['python3-pip'],
}
