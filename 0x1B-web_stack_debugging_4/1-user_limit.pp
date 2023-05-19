# login with the holberton user and open a file without any error message 
exec { 'Fix hard limit':
  command => '/usr/bin/env sed -i "s/4/20000/; s/5/20000/" /etc/security/limits.conf'
}
