# A puppet manifest that Increases the amount of traffic an Nginx server can handle.

exec {'update max open files limit setting':
  command => 'sed -i "s/15/10000/" /etc/default/nginx && sudo service restart nginx',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games',
}
