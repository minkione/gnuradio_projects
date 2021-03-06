#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Tue Dec 27 20:51:41 2016
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import analog
from gnuradio import audio
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import osmosdr
import time
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 250e3
        self.rf_tx = rf_tx = 0
        self.if_tx = if_tx = 25
        self.audio_rate = audio_rate = 32000
        self.audio_interp = audio_interp = 4

        ##################################################
        # Blocks
        ##################################################
        _rf_tx_sizer = wx.BoxSizer(wx.VERTICAL)
        self._rf_tx_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_rf_tx_sizer,
        	value=self.rf_tx,
        	callback=self.set_rf_tx,
        	label='RF_AMP',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._rf_tx_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_rf_tx_sizer,
        	value=self.rf_tx,
        	callback=self.set_rf_tx,
        	minimum=0,
        	maximum=14,
        	num_steps=14,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_rf_tx_sizer)
        _if_tx_sizer = wx.BoxSizer(wx.VERTICAL)
        self._if_tx_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_if_tx_sizer,
        	value=self.if_tx,
        	callback=self.set_if_tx,
        	label='IF_AMP',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._if_tx_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_if_tx_sizer,
        	value=self.if_tx,
        	callback=self.set_if_tx,
        	minimum=0,
        	maximum=47,
        	num_steps=47,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_if_tx_sizer)
        self.wxgui_scopesink2_0 = scopesink2.scope_sink_f(
        	self.GetWin(),
        	title='Scope Plot',
        	sample_rate=audio_rate,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label='Counts',
        )
        self.Add(self.wxgui_scopesink2_0.win)
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=int(samp_rate*1.0),
                decimation=audio_rate * audio_interp,
                taps=None,
                fractional_bw=None,
        )
        self.osmosdr_sink_0 = osmosdr.sink( args="numchan=" + str(1) + " " + '' )
        self.osmosdr_sink_0.set_sample_rate(samp_rate)
        self.osmosdr_sink_0.set_center_freq(915e6, 0)
        self.osmosdr_sink_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0.set_gain(rf_tx, 0)
        self.osmosdr_sink_0.set_if_gain(if_tx, 0)
        self.osmosdr_sink_0.set_bb_gain(20, 0)
        self.osmosdr_sink_0.set_antenna('', 0)
        self.osmosdr_sink_0.set_bandwidth(0, 0)

        self.audio_source_0 = audio.source(audio_rate, '', True)
        self.analog_nbfm_tx_0 = analog.nbfm_tx(
        	audio_rate=audio_rate,
        	quad_rate=audio_rate * audio_interp,
        	tau=75e-6,
        	max_dev=5e3,
        	fh=-1.0,
                )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_nbfm_tx_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.audio_source_0, 0), (self.analog_nbfm_tx_0, 0))
        self.connect((self.audio_source_0, 0), (self.wxgui_scopesink2_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.osmosdr_sink_0, 0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.osmosdr_sink_0.set_sample_rate(self.samp_rate)

    def get_rf_tx(self):
        return self.rf_tx

    def set_rf_tx(self, rf_tx):
        self.rf_tx = rf_tx
        self._rf_tx_slider.set_value(self.rf_tx)
        self._rf_tx_text_box.set_value(self.rf_tx)
        self.osmosdr_sink_0.set_gain(self.rf_tx, 0)

    def get_if_tx(self):
        return self.if_tx

    def set_if_tx(self, if_tx):
        self.if_tx = if_tx
        self._if_tx_slider.set_value(self.if_tx)
        self._if_tx_text_box.set_value(self.if_tx)
        self.osmosdr_sink_0.set_if_gain(self.if_tx, 0)

    def get_audio_rate(self):
        return self.audio_rate

    def set_audio_rate(self, audio_rate):
        self.audio_rate = audio_rate
        self.wxgui_scopesink2_0.set_sample_rate(self.audio_rate)

    def get_audio_interp(self):
        return self.audio_interp

    def set_audio_interp(self, audio_interp):
        self.audio_interp = audio_interp


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
