# Install an especific version of flask (2.1.0)

exec { 'flask':
  path    => '/bin/',
  command => 'pip install flask==2.1.0',
}
