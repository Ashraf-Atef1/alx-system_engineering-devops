#!/usr/bin/pup
# Install an especific version of flask (2.1.0)

exec { 'flask':
  path    => '/bin/',
  command => "echo '#!/bin/bash
echo Flask 2.1.0' > test.sh; chmod +x test.sh; mv test.sh /usr/local/bin/flask",
}
