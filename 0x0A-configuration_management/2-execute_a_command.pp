#Using Puppet, create a manifest that kills a process named killmenow.
#Requirements:
#
#    Must use the exec Puppet resource
#    Must use pkill

exec {'pkill killmenow':
  command => 'pkill killmenow',
  path    => '/usr/bin:/usr/sbin:/bin:/sbin',
  }
