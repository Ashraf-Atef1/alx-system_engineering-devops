# create a manifest that kills

exec { 'install_flask':
  path    => '/bin/',
  command => 'pkill 0 killmenow',
}
