file { '/etc/ssh/ssh_config':
  ensure  => present,
  content => "# Managed by Puppet\n\nHost *\n    IdentityFile ~/.ssh/school\n
	  		PasswordAuthentication no\n",
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
}
