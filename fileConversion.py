'''
Created on Mar 11, 2017
finds whether file needs to be converted
converts if neccessary
output must be a valid wav file, boolean
indicating if there was a conversion
@author: abe
'''
#! /bin/env python
import numpy
import scipy.io.wavfile as read_wav
import pymedia.audio.acodec as acodec
import pymedia.muxer as muxer
import time, wave, string, os

def fileConversion(filename):
    wavFile=False
    file=filename.lower()
    def Wav():
        print "stop"
        #converting pcm aiff and dsp if needed
        
    def decompressWAV( fname ):
        snd=None
        fname1= str.split( fname, '.' )
        fname2= string.join( fname1[ : len( fname1 )- 1 ] )
        # Open demuxer first
        
        dm= muxer.Demuxer( fname1[ -1 ].lower() )
        dec= None
        f= open( fname, 'rb' )
        s= " "
        while len( s ):
            s= f.read( 20000 )
            if len( s ):
                frames= dm.parse( s )
                for fr in frames:
                    if dec== None:
                        # Open decoder
    
                        dec= acodec.Decoder( dm.streams[ 0 ] )
                    r= dec.decode( fr[ 1 ] )
                    if r and r.data:
                        if snd== None:
                            snd= wave.open( fname2+ '.wav', 'wb' )
                            snd.setparams( (r.channels, 2, r.sample_rate, 0, 'NONE','') )
                        
                        snd.writeframes( r.data )
        return snd
    
    if file.endswith('.wav'):
            snd=filename
            wavFile=True
        
    else:
        if file.endswith('.pcm') | file.endswith('.aiff') | file.endswith('dsp'):
            Wav()
        else:
            snd=decompressWAV(file)

    return snd,wavFile

file1,wav=fileConversion('Woof-woof-woof.mp3')
if (wav==True):
    print "True"
print file1
