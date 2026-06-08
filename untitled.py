#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# Author: informatica
# GNU Radio version: 3.10.9.2

from PyQt5 import Qt
from gnuradio import qtgui
from PyQt5 import QtCore
from gnuradio import analog
from gnuradio import blocks
import numpy
from gnuradio import digital
from gnuradio import fec
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import sip



class untitled(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "untitled")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)

        ##################################################
        # Variables
        ##################################################
        self.variable_constellation_3 = variable_constellation_3 = digital.constellation_8psk().base()
        self.variable_constellation_3.set_npwr(1.0)
        self.variable_constellation_2 = variable_constellation_2 = digital.constellation_qpsk().base()
        self.variable_constellation_2.set_npwr(1.0)
        self.variable_constellation_1 = variable_constellation_1 = digital.constellation_bpsk().base()
        self.variable_constellation_1.set_npwr(1.0)
        self.samp_rate = samp_rate = 32000
        self.noise_amp1 = noise_amp1 = 1
        self.noise_amp = noise_amp = 0.1993

        ##################################################
        # Blocks
        ##################################################

        self._noise_amp_range = qtgui.Range(0.01, 1, 0.01, 0.1993, 200)
        self._noise_amp_win = qtgui.RangeWidget(self._noise_amp_range, self.set_noise_amp, "'noise_amp'", "eng_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._noise_amp_win)
        self.qtgui_number_sink_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            3,
            None # parent
        )
        self.qtgui_number_sink_0.set_update_time(0.10)
        self.qtgui_number_sink_0.set_title("")

        labels = ['BPSK', 'QPSK', '8PSK', '', '',
            '', '', '', '', '']
        units = ['', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "white"), ("black", "white"), ("black", "white"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(3):
            self.qtgui_number_sink_0.set_min(i, -7)
            self.qtgui_number_sink_0.set_max(i, 0)
            self.qtgui_number_sink_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0.set_label(i, labels[i])
            self.qtgui_number_sink_0.set_unit(i, units[i])
            self.qtgui_number_sink_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0.enable_autoscale(False)
        self._qtgui_number_sink_0_win = sip.wrapinstance(self.qtgui_number_sink_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_number_sink_0_win)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
            1024, #size
            "", #name
            3, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis((-2), 2)
        self.qtgui_const_sink_x_0.set_x_axis((-2), 2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(False)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)


        labels = ['BPSK', 'QPSK', '8PSK', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        styles = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(3):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_const_sink_x_0_win)
        self.fec_ber_bf_0_1 = fec.ber_bf(False, 100, -7.0)
        self.fec_ber_bf_0_0 = fec.ber_bf(False, 100, -7.0)
        self.fec_ber_bf_0 = fec.ber_bf(False, 100, -7.0)
        self.digital_constellation_decoder_cb_1 = digital.constellation_decoder_cb(variable_constellation_1)
        self.digital_constellation_decoder_cb_0_0 = digital.constellation_decoder_cb(variable_constellation_3)
        self.digital_constellation_decoder_cb_0 = digital.constellation_decoder_cb(variable_constellation_2)
        self.digital_chunks_to_symbols_xx_0_1 = digital.chunks_to_symbols_bc(variable_constellation_2.points(), 1)
        self.digital_chunks_to_symbols_xx_0_0 = digital.chunks_to_symbols_bc(variable_constellation_3.points(), 1)
        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bc(variable_constellation_1.points(), 1)
        self.blocks_throttle2_0_1 = blocks.throttle( gr.sizeof_char*1, samp_rate, True, 0 if "auto" == "auto" else max( int(float(0.1) * samp_rate) if "auto" == "time" else int(0.1), 1) )
        self.blocks_throttle2_0_0 = blocks.throttle( gr.sizeof_char*1, samp_rate, True, 0 if "auto" == "auto" else max( int(float(0.1) * samp_rate) if "auto" == "time" else int(0.1), 1) )
        self.blocks_throttle2_0 = blocks.throttle( gr.sizeof_char*1, samp_rate, True, 0 if "auto" == "auto" else max( int(float(0.1) * samp_rate) if "auto" == "time" else int(0.1), 1) )
        self.blocks_pack_k_bits_bb_1_1 = blocks.pack_k_bits_bb(8)
        self.blocks_pack_k_bits_bb_1_0 = blocks.pack_k_bits_bb(8)
        self.blocks_pack_k_bits_bb_1 = blocks.pack_k_bits_bb(8)
        self.blocks_pack_k_bits_bb_0_1 = blocks.pack_k_bits_bb(8)
        self.blocks_pack_k_bits_bb_0_0 = blocks.pack_k_bits_bb(8)
        self.blocks_pack_k_bits_bb_0 = blocks.pack_k_bits_bb(8)
        self.blocks_add_xx_0_1 = blocks.add_vcc(1)
        self.blocks_add_xx_0_0 = blocks.add_vcc(1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.analog_random_source_x_0_1 = blocks.vector_source_b(list(map(int, numpy.random.randint(0, 4, 10000))), True)
        self.analog_random_source_x_0_0 = blocks.vector_source_b(list(map(int, numpy.random.randint(0, 8, 10000))), True)
        self.analog_random_source_x_0 = blocks.vector_source_b(list(map(int, numpy.random.randint(0, 2, 10000))), True)
        self.analog_noise_source_x_0_1 = analog.noise_source_c(analog.GR_GAUSSIAN, noise_amp, 0)
        self.analog_noise_source_x_0_0 = analog.noise_source_c(analog.GR_GAUSSIAN, noise_amp, 0)
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, noise_amp, 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0_0, 1))
        self.connect((self.analog_noise_source_x_0_0, 0), (self.blocks_add_xx_0_1, 1))
        self.connect((self.analog_noise_source_x_0_1, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_throttle2_0, 0))
        self.connect((self.analog_random_source_x_0_0, 0), (self.blocks_throttle2_0_0, 0))
        self.connect((self.analog_random_source_x_0_1, 0), (self.blocks_throttle2_0_1, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.digital_constellation_decoder_cb_1, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_const_sink_x_0, 0))
        self.connect((self.blocks_add_xx_0_0, 0), (self.digital_constellation_decoder_cb_0_0, 0))
        self.connect((self.blocks_add_xx_0_0, 0), (self.qtgui_const_sink_x_0, 2))
        self.connect((self.blocks_add_xx_0_1, 0), (self.digital_constellation_decoder_cb_0, 0))
        self.connect((self.blocks_add_xx_0_1, 0), (self.qtgui_const_sink_x_0, 1))
        self.connect((self.blocks_pack_k_bits_bb_0, 0), (self.fec_ber_bf_0_0, 0))
        self.connect((self.blocks_pack_k_bits_bb_0_0, 0), (self.fec_ber_bf_0_1, 1))
        self.connect((self.blocks_pack_k_bits_bb_0_1, 0), (self.fec_ber_bf_0_1, 0))
        self.connect((self.blocks_pack_k_bits_bb_1, 0), (self.fec_ber_bf_0_0, 1))
        self.connect((self.blocks_pack_k_bits_bb_1_0, 0), (self.fec_ber_bf_0, 1))
        self.connect((self.blocks_pack_k_bits_bb_1_1, 0), (self.fec_ber_bf_0, 0))
        self.connect((self.blocks_throttle2_0, 0), (self.blocks_pack_k_bits_bb_1, 0))
        self.connect((self.blocks_throttle2_0, 0), (self.digital_chunks_to_symbols_xx_0, 0))
        self.connect((self.blocks_throttle2_0_0, 0), (self.blocks_pack_k_bits_bb_0_0, 0))
        self.connect((self.blocks_throttle2_0_0, 0), (self.digital_chunks_to_symbols_xx_0_0, 0))
        self.connect((self.blocks_throttle2_0_1, 0), (self.blocks_pack_k_bits_bb_1_0, 0))
        self.connect((self.blocks_throttle2_0_1, 0), (self.digital_chunks_to_symbols_xx_0_1, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0_0, 0), (self.blocks_add_xx_0_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0_1, 0), (self.blocks_add_xx_0_1, 0))
        self.connect((self.digital_constellation_decoder_cb_0, 0), (self.blocks_pack_k_bits_bb_1_1, 0))
        self.connect((self.digital_constellation_decoder_cb_0_0, 0), (self.blocks_pack_k_bits_bb_0_1, 0))
        self.connect((self.digital_constellation_decoder_cb_1, 0), (self.blocks_pack_k_bits_bb_0, 0))
        self.connect((self.fec_ber_bf_0, 0), (self.qtgui_number_sink_0, 1))
        self.connect((self.fec_ber_bf_0_0, 0), (self.qtgui_number_sink_0, 0))
        self.connect((self.fec_ber_bf_0_1, 0), (self.qtgui_number_sink_0, 2))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "untitled")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_variable_constellation_3(self):
        return self.variable_constellation_3

    def set_variable_constellation_3(self, variable_constellation_3):
        self.variable_constellation_3 = variable_constellation_3
        self.digital_constellation_decoder_cb_0_0.set_constellation(self.variable_constellation_3)

    def get_variable_constellation_2(self):
        return self.variable_constellation_2

    def set_variable_constellation_2(self, variable_constellation_2):
        self.variable_constellation_2 = variable_constellation_2
        self.digital_constellation_decoder_cb_0.set_constellation(self.variable_constellation_2)

    def get_variable_constellation_1(self):
        return self.variable_constellation_1

    def set_variable_constellation_1(self, variable_constellation_1):
        self.variable_constellation_1 = variable_constellation_1
        self.digital_constellation_decoder_cb_1.set_constellation(self.variable_constellation_1)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle2_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle2_0_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle2_0_1.set_sample_rate(self.samp_rate)

    def get_noise_amp1(self):
        return self.noise_amp1

    def set_noise_amp1(self, noise_amp1):
        self.noise_amp1 = noise_amp1

    def get_noise_amp(self):
        return self.noise_amp

    def set_noise_amp(self, noise_amp):
        self.noise_amp = noise_amp
        self.analog_noise_source_x_0.set_amplitude(self.noise_amp)
        self.analog_noise_source_x_0_0.set_amplitude(self.noise_amp)
        self.analog_noise_source_x_0_1.set_amplitude(self.noise_amp)




def main(top_block_cls=untitled, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
