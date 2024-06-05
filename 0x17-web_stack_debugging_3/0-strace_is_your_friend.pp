# puppet file to fix the wordpress problem

exec { 'Fix miss-spling problem':
  command  => 'sudo sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
  provider => shell,
}
