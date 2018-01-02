#!/bin/sh
{
sleep 5
echo "remote"
sleep 5
echo "SecureLink!"
sleep 5
echo "request system software add ftp://192.168.0.1/jinstall-ex-4200-15.1R5.5-domestic-signed.tgz"
sleep 360
echo "request system reboot"
sleep 20
echo ""
sleep 2
echo ""
sleep 2
} | telnet $1

sleep 360

{
sleep 5
echo "remote"
sleep 5
echo "SecureLink!"
sleep 2
echo ""
sleep 1
echo "request system snapshot slice alternate"
sleep 60
echo ""
sleep 2
echo "show version"
sleep 5
} | telnet $1

$SHELL
