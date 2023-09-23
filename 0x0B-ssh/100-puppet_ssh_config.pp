file { '/home/ubuntu':
  ensure => 'directory',
  mode   => '0755',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file { '/home/ubuntu/.ssh':
  ensure => 'directory',
  mode   => '0700',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file { '/home/ubuntu/.ssh/config':
  ensure  => 'file',
  content => "
    Host *
    IdentityFile ~/.ssh/school
    PasswordAuthentication no
  ",
  mode    => '0600',
  owner   => 'ubuntu',
  group   => 'ubuntu',
}

