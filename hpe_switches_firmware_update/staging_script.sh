#!/bin/sh
{
sleep 1
echo ""
sleep 2
echo ""
sleep 1
echo "copy tftp flash 192.168.0.1 WC_16_04_0008.swi primary oobm"
sleep 1
echo "y"
sleep 50
echo "copy flash flash secondary"
sleep 20
echo "reboot"
sleep 2
echo "y"
sleep 2
} | telnet $1

sleep 360

{
sleep 1
echo ""
sleep 2
echo ""
sleep 2
echo ""
sleep 1
echo ""
sleep 2
echo "chassislocate blink"
sleep 2
echo "show version"
sleep 5
} | telnet $1

$SHELL
