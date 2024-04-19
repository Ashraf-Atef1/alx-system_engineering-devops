# create a manifest that kills

exec { 'pkill killmenow':
  path    => '/bin/',
  command => 'pkill killmenow',
}
