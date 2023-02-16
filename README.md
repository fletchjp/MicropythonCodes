# MicropythonCodes
 Micropython codes developed for model railway applications

## Introduction

I started to work with Micropython following Duncan Greenwood's talk on Micropython for CBUS.

I had not up until then thought of using Micropython for the Raspberry Pi Pico. I had concentrated instead on using the Arduino-Pico software.

I have started by getting a version of Duncan's code working for some of my Pico hardware for which I had found no Arduino-Pico solution.

I have had some success with that although I have yet to test it out with CBUS and have not developed a working application.

I do have some useful understanding and want to put the codes onto Github.

I am currently using Thonny to edit my codes.

John Fletcher February 2023

## Hardware

I have two copies of the Pico Hat Expansion from sb Components. These make it possible to combine a Raspberry Pi Pico with a HAT designed for a Raspberry Pi.

I also obtained a HAT which has CAN and RS485 ports with the necessary hardware to support communication.

I had obtained one some time ago and been unable to find any software for the Arduino-Pico C++ system which would enable me to use the ports.

I have now been able to make use of the HAT with code written in Micropython. I am using Micropython for CBUS written by Duncan Greenwood.

## keypad examples

Examples with a 4 by 4 keypad attached to the Raspberry Pi Pico.

## uasyncio examples

These are examples of how to use uasyncio to control different tasks.

## uart_examples

These are examples of the codes sending simple messages over the RS485 connection.
