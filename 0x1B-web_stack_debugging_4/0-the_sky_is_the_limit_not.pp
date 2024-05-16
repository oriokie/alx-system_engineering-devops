# Puppet file for increasing the number of requests
# the nginx server can handle

# increasing the ULIMIT of the default file
exec { 'increasing-the-ULIMIT':
    command => 'sed -i "s/15/4096/" /etc/default/nginx',
    path    => '/usr/local/bin:/bin/'
} ->

# Restart Nginx
exec { 'restart-nginx-service':
    command => 'nginx restart',
    path    => '/etc/init.d/'
}
