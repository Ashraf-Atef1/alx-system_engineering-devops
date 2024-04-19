# Install an especific version of flask (2.1.0)

package {'flas':
  ensure   => '2.1.0',
  provider => 'pip'
}
