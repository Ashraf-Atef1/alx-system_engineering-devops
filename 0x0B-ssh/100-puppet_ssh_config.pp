# Changes to config Puppet

file_line { 'refuse_to_authenticate_using_a_password':
  path => '/etc/ssh/ssh_config',
  line => '  PasswordAuthentication no',
}

file_line { 'IdentityFile':
  path => '/etc/ssh/ssh_config',
  line => '  IdentityFile ~/.ssh/school',
}
