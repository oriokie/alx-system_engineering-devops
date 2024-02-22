#Using Puppet, to create a manifect that kills a process named killmenow
exec {  'kill':
    command => '/usr/bin/pkill -f killmenow'
}
