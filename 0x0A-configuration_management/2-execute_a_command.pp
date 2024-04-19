# create a manifest that kills

exec { 'install_flask':
  command => 'pkill 0 killmenow',
}
