#!/usr/bin/pup
# Install an especific version of flask (2.1.0)

exec { 'flask':
  path    => '/bin/',
  command => 'alias flask="echo Flask 2.1.0;#"',
}
