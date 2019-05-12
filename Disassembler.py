import threading
import time

class Disassemble:
  pc = 0
  # instructions = [0x00,0x00,0x01,0xC3,0xC3,0x00]

  instructions = [0x00,0x00,0x00,0xC3,0xD4,0x18,0x00,0x00,0xF5,0xC5,0xD5,0xE5,0xC3,0x8C,0x00,0x00, # 0x00000000 ................
  0xF5,0xC5,0xD5,0xE5,0x3E,0x80,0x32,0x72,0x20,0x21,0xC0,0x20,0x35,0xCD,0xCD,0x17, # 0x00000010 ......2r !. 5...
  0xDB,0x01,0x0F,0xDA,0x67,0x00,0x3A,0xEA,0x20,0xA7,0xCA,0x42,0x00,0x3A,0xEB,0x20, # 0x00000020 ....g.:. ..B.:.
  0xFE,0x99,0xCA,0x3E,0x00,0xC6,0x01,0x27,0x32,0xEB,0x20,0xCD,0x47,0x19,0xAF,0x32, # 0x00000030 .......'2. .G..2
  0xEA,0x20,0x3A,0xE9,0x20,0xA7,0xCA,0x82,0x00,0x3A,0xEF,0x20,0xA7,0xC2,0x6F,0x00, # 0x00000040 . :. ....:. ..o.
  0x3A,0xEB,0x20,0xA7,0xC2,0x5D,0x00,0xCD,0xBF,0x0A,0xC3,0x82,0x00,0x3A,0x93,0x20, # 0x00000050 :. ..].......:.
  0xA7,0xC2,0x82,0x00,0xC3,0x65,0x07,0x3E,0x01,0x32,0xEA,0x20,0xC3,0x3F,0x00,0xCD, # 0x00000060 .....e...2. .?..
  0x40,0x17,0x3A,0x32,0x20,0x32,0x80,0x20,0xCD,0x00,0x01,0xCD,0x48,0x02,0xCD,0x13, # 0x00000070 @.:2 2. ....H...
  0x09,0x00,0xE1,0xD1,0xC1,0xF1,0xFB,0xC9,0x00,0x00,0x00,0x00,0xAF,0x32,0x72,0x20, # 0x00000080 .............2r
  0x3A,0xE9,0x20,0xA7,0xCA,0x82,0x00,0x3A,0xEF,0x20,0xA7,0xC2,0xA5,0x00,0x3A,0xC1, # 0x00000090 :. ....:. ....:.
  0x20,0x0F,0xD2,0x82,0x00,0x21,0x20,0x20,0xCD,0x4B,0x02,0xCD,0x41,0x01,0xC3,0x82, # 0x000000A0  ....!  .K..A...
  0x00,0xCD,0x86,0x08,0xE5,0x7E,0x23,0x66,0x6F,0x22,0x09,0x20,0x22,0x0B,0x20,0xE1, # 0x000000B0 .....~#fo". ". .
  0x2B,0x7E,0xFE,0x03,0xC2,0xC8,0x00,0x3D,0x32,0x08,0x20,0xFE,0xFE,0x3E,0x00,0xC2, # 0x000000C0 +~.....=2. .....
  0xD3,0x00,0x3C,0x32,0x0D,0x20,0xC9,0x3E,0x02,0x32,0xFB,0x21,0x32,0xFB,0x22,0xC3, # 0x000000D0 ...2. ...2.!2.".
  0xE4,0x08,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 0x000000E0 ................
  0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 0x000000F0 ................
  0x21,0x02,0x20,0x7E,0xA7,0xC2,0x38,0x15,0xE5,0x3A,0x06,0x20,0x6F,0x3A,0x67,0x20, # 0x00000100 !. ~..8..:. o:g
  0x67,0x7E,0xA7,0xE1,0xCA,0x36,0x01,0x23,0x23,0x7E,0x23,0x46,0xE6,0xFE,0x07,0x07, # 0x00000110 g~...6.##~#F....
  0x07,0x5F,0x16,0x00,0x21,0x00,0x1C,0x19,0xEB,0x78,0xA7,0xC4,0x3B,0x01,0x2A,0x0B, # 0x00000120 ._..!....x..;.*.
  0x20,0x06,0x10,0xCD,0xD3,0x15,0xAF,0x32,0x00,0x20,0xC9,0x21,0x30,0x00,0x19,0xEB, # 0x00000130  ......2. .!0...
  0xC9,0x3A,0x68,0x20,0xA7,0xC8,0x3A,0x00,0x20,0xA7,0xC0,0x3A,0x67,0x20,0x67,0x3A, # 0x00000140 .:h ..:. ..:g g:
  0x06,0x20,0x16,0x02,0x3C,0xFE,0x37,0xCC,0xA1,0x01,0x6F,0x46,0x05,0xC2,0x54,0x01, # 0x00000150 . ....7...oF..T.
  0x32,0x06,0x20,0xCD,0x7A,0x01,0x61,0x22,0x0B,0x20,0x7D,0xFE,0x28,0xDA,0x71,0x19, # 0x00000160 2. .z.a". }.(.q.
  0x7A,0x32,0x04,0x20,0x3E,0x01,0x32,0x00,0x20,0xC9,0x16,0x00,0x7D,0x21,0x09,0x20, # 0x00000170 z2. ..2. ...}!.
  0x46,0x23,0x4E,0xFE,0x0B,0xFA,0x94,0x01,0xDE,0x0B,0x5F,0x78,0xC6,0x10,0x47,0x7B, # 0x00000180 F#N......._x..G{
  0x14,0xC3,0x83,0x01,0x68,0xA7,0xC8,0x5F,0x79,0xC6,0x10,0x4F,0x7B,0x3D,0xC3,0x95, # 0x00000190 ....h.._y..O{=..
  0x01,0x15,0xCA,0xCD,0x01,0x21,0x06,0x20,0x36,0x00,0x23,0x4E,0x36,0x00,0xCD,0xD9, # 0x000001A0 .....!. 6.#N6...
  0x01,0x21,0x05,0x20,0x7E,0x3C,0xE6,0x01,0x77,0xAF,0x21,0x67,0x20,0x66,0xC9,0x00, # 0x000001B0 .!. ~...w.!g f..
  0x21,0x00,0x21,0x06,0x37,0x36,0x01,0x23,0x05,0xC2,0xC5,0x01,0xC9,0xE1,0xC9,0x3E, # 0x000001C0 !.!.76.#........
  0x01,0x06,0xE0,0x21,0x02,0x24,0xC3,0xCC,0x14,0x23,0x46,0x23,0x79,0x86,0x77,0x23, # 0x000001D0 ...!.$...#F#y.w#
  0x78,0x86,0x77,0xC9,0x06,0xC0,0x11,0x00,0x1B,0x21,0x00,0x20,0xC3,0x32,0x1A,0x21, # 0x000001E0 x.w......!. .2.!
  0x42,0x21,0xC3,0xF8,0x01,0x21,0x42,0x22,0x0E,0x04,0x11,0x20,0x1D,0xD5,0x06,0x2C, # 0x000001F0 B!...!B"... ...,
  0xCD,0x32,0x1A,0xD1,0x0D,0xC2,0xFD,0x01,0xC9,0x3E,0x01,0xC3,0x1B,0x02,0x3E,0x01, # 0x00000200 .2..............
  0xC3,0x14,0x02,0xAF,0x11,0x42,0x22,0xC3,0x1E,0x02,0xAF,0x11,0x42,0x21,0x32,0x81, # 0x00000210 .....B".....B!2.
  0x20,0x01,0x02,0x16,0x21,0x06,0x28,0x3E,0x04,0xF5,0xC5,0x3A,0x81,0x20,0xA7,0xC2, # 0x00000220  ...!.(....:. ..
  0x42,0x02,0xCD,0x69,0x1A,0xC1,0xF1,0x3D,0xC8,0xD5,0x11,0xE0,0x02,0x19,0xD1,0xC3, # 0x00000230 B..i...=........
  0x29,0x02,0xCD,0x7C,0x14,0xC3,0x35,0x02,0x21,0x10,0x20,0x7E,0xFE,0xFF,0xC8,0xFE, # 0x00000240 )..|..5.!. ~....
  0xFE,0xCA,0x81,0x02,0x23,0x46,0x4F,0xB0,0x79,0xC2,0x77,0x02,0x23,0x7E,0xA7,0xC2, # 0x00000250 ....#FO.y.w.#~..
  0x88,0x02,0x23,0x5E,0x23,0x56,0xE5,0xEB,0xE5,0x21,0x6F,0x02,0xE3,0xD5,0xE9,0xE1, # 0x00000260 ..#^#V...!o.....
  0x11,0x0C,0x00,0x19,0xC3,0x4B,0x02,0x05,0x04,0xC2,0x7D,0x02,0x3D,0x05,0x70,0x2B, # 0x00000270 .....K....}.=.p+
  0x77,0x11,0x10,0x00,0x19,0xC3,0x4B,0x02,0x35,0x2B,0x2B,0xC3,0x81,0x02,0xE1,0x23, # 0x00000280 w.....K.5++....#
  0x7E,0xFE,0xFF,0xCA,0x3B,0x03,0x23,0x35,0xC0,0x47,0xAF,0x32,0x68,0x20,0x32,0x69, # 0x00000290 ~...;.#5.G.2h 2i
  0x20,0x3E,0x30,0x32,0x6A,0x20,0x78,0x36,0x05,0x23,0x35,0xC2,0x9B,0x03,0x2A,0x1A, # 0x000002A0  .02j x6.#5...*.
  0x20,0x06,0x10,0xCD,0x24,0x14,0x21,0x10,0x20,0x11,0x10,0x1B,0x06,0x10,0xCD,0x32, # 0x000002B0  ...$.!. ......2
  0x1A,0x06,0x00,0xCD,0xDC,0x19,0x3A,0x6D,0x20,0xA7,0xC0,0x3A,0xEF,0x20,0xA7,0xC8, # 0x000002C0 ......:m ..:. ..
  0x31,0x00,0x24,0xFB,0xCD,0xD7,0x19,0xCD,0x2E,0x09,0xA7,0xCA,0x6D,0x16,0xCD,0xE7, # 0x000002D0 1.$.........m...
  0x18,0x7E,0xA7,0xCA,0x2C,0x03,0x3A,0xCE,0x20,0xA7,0xCA,0x2C,0x03,0x3A,0x67,0x20, # 0x000002E0 .~..,.:. ..,.:g
  0xF5,0x0F,0xDA,0x32,0x03,0xCD,0x0E,0x02,0xCD,0x78,0x08,0x73,0x23,0x72,0x2B,0x2B, # 0x000002F0 ...2.....x.s#r++
  0x70,0x00,0xCD,0xE4,0x01,0xF1,0x0F,0x3E,0x21,0x06,0x00,0xD2,0x12,0x03,0x06,0x20, # 0x00000300 p.......!......
  0x3E,0x22,0x32,0x67,0x20,0xCD,0xB6,0x0A,0xAF,0x32,0x11,0x20,0x78,0xD3,0x05,0x3C, # 0x00000310 ."2g ....2. x...
  0x32,0x98,0x20,0xCD,0xD6,0x09,0xCD,0x7F,0x1A,0xC3,0xF9,0x07,0xCD,0x7F,0x1A,0xC3, # 0x00000320 2. .............
  0x17,0x08,0xCD,0x09,0x02,0xC3,0xF8,0x02,0x00,0x00,0x00,0x21,0x68,0x20,0x36,0x01, # 0x00000330 ...........!h 6.
  0x23,0x7E,0xA7,0xC3,0xB0,0x03,0x00,0x2B,0x36,0x01,0x3A,0x1B,0x20,0x47,0x3A,0xEF, # 0x00000340 #~.....+6.:. G:.
  0x20,0xA7,0xC2,0x63,0x03,0x3A,0x1D,0x20,0x0F,0xDA,0x81,0x03,0x0F,0xDA,0x8E,0x03, # 0x00000350  ..c.:. ........
  0xC3,0x6F,0x03,0xCD,0xC0,0x17,0x07,0x07,0xDA,0x81,0x03,0x07,0xDA,0x8E,0x03,0x21, # 0x00000360 .o.............!
  0x18,0x20,0xCD,0x3B,0x1A,0xCD,0x47,0x1A,0xCD,0x39,0x14,0x3E,0x00,0x32,0x12,0x20, # 0x00000370 . .;..G..9...2.
  0xC9,0x78,0xFE,0xD9,0xCA,0x6F,0x03,0x3C,0x32,0x1B,0x20,0xC3,0x6F,0x03,0x78,0xFE, # 0x00000380 .x...o..2. .o.x.
  0x30,0xCA,0x6F,0x03,0x3D,0x32,0x1B,0x20,0xC3,0x6F,0x03,0x3C,0xE6,0x01,0x32,0x15, # 0x00000390 0.o.=2. .o....2.
  0x20,0x07,0x07,0x07,0x07,0x21,0x70,0x1C,0x85,0x6F,0x22,0x18,0x20,0xC3,0x6F,0x03, # 0x000003A0  ....!p..o". .o.
  0xC2,0x4A,0x03,0x23,0x35,0xC2,0x4A,0x03,0xC3,0x46,0x03,0x11,0x2A,0x20,0xCD,0x06, # 0x000003B0 .J.#5.J..F..* ..
  0x1A,0xE1,0xD0,0x23,0x7E,0xA7,0xC8,0xFE,0x01,0xCA,0xFA,0x03,0xFE,0x02,0xCA,0x0A, # 0x000003C0 ...#~...........
  0x04,0x23,0xFE,0x03,0xC2,0x2A,0x04,0x35,0xCA,0x36,0x04,0x7E,0xFE,0x0F,0xC0,0xE5, # 0x000003D0 .#...*.5.6.~....
  0xCD,0x30,0x04,0xCD,0x52,0x14,0xE1,0x23,0x34,0x23,0x23,0x35,0x35,0x23,0x35,0x35, # 0x000003E0 .0..R..#4##55#55
  0x35,0x23,0x36,0x08,0xCD,0x30,0x04,0xC3,0x00,0x14,0x3C,0x77,0x3A,0x1B,0x20,0xC6, # 0x000003F0 5#6..0.....w:. .
  0x08,0x32,0x2A,0x20,0xCD,0x30,0x04,0xC3,0x00,0x14,0xCD,0x30,0x04,0xD5,0xE5,0xC5, # 0x00000400 .2* .0.....0....
  0xCD,0x52,0x14,0xC1,0xE1,0xD1,0x3A,0x2C,0x20,0x85,0x6F,0x32,0x29,0x20,0xCD,0x91, # 0x00000410 .R....:, .o2) ..
  0x14,0x3A,0x61,0x20,0xA7,0xC8,0x32,0x02,0x20,0xC9,0xFE,0x05,0xC8,0xC3,0x36,0x04, # 0x00000420 .:a ..2. .....6.
  0x21,0x27,0x20,0xC3,0x3B,0x1A,0xCD,0x30,0x04,0xCD,0x52,0x14,0x21,0x25,0x20,0x11, # 0x00000430 !' .;..0..R.!% .
  0x25,0x1B,0x06,0x07,0xCD,0x32,0x1A,0x2A,0x8D,0x20,0x2C,0x7D,0xFE,0x63,0xDA,0x53, # 0x00000440 %....2.*. ,}.c.S
  0x04,0x2E,0x54,0x22,0x8D,0x20,0x2A,0x8F,0x20,0x2C,0x22,0x8F,0x20,0x3A,0x84,0x20, # 0x00000450 ..T". *. ,". :.
  0xA7,0xC0,0x7E,0xE6,0x01,0x01,0x29,0x02,0xC2,0x6E,0x04,0x01,0xE0,0xFE,0x21,0x8A, # 0x00000460 ..~...)..n....!.
  0x20,0x71,0x23,0x23,0x70,0xC9,0xE1,0x3A,0x32,0x1B,0x32,0x32,0x20,0x2A,0x38,0x20, # 0x00000470  q##p..:2.22 *8
  0x7D,0xB4,0xC2,0x8A,0x04,0x2B,0x22,0x38,0x20,0xC9,0x11,0x35,0x20,0x3E,0xF9,0xCD, # 0x00000480 }....+"8 ..5 ...
  0x50,0x05,0x3A,0x46,0x20,0x32,0x70,0x20,0x3A,0x56,0x20,0x32,0x71,0x20,0xCD,0x63, # 0x00000490 P.:F 2p :V 2q .c
  0x05,0x3A,0x78,0x20,0xA7,0x21,0x35,0x20,0xC2,0x5B,0x05,0x11,0x30,0x1B,0x21,0x30, # 0x000004A0 .:x .!5 .[..0.!0
  0x20,0x06,0x10,0xC3,0x32,0x1A,0xE1,0x3A,0x6E,0x20,0xA7,0xC0,0x3A,0x80,0x20,0xFE, # 0x000004B0  ...2..:n ..:. .
  0x01,0xC0,0x11,0x45,0x20,0x3E,0xED,0xCD,0x50,0x05,0x3A,0x36,0x20,0x32,0x70,0x20, # 0x000004C0 ...E ...P.:6 2p
  0x3A,0x56,0x20,0x32,0x71,0x20,0xCD,0x63,0x05,0x3A,0x76,0x20,0xFE,0x10,0xDA,0xE7, # 0x000004D0 :V 2q .c.:v ....
  0x04,0x3A,0x48,0x1B,0x32,0x76,0x20,0x3A,0x78,0x20,0xA7,0x21,0x45,0x20,0xC2,0x5B, # 0x000004E0 .:H.2v :x .!E .[
  0x05,0x11,0x40,0x1B,0x21,0x40,0x20,0x06,0x10,0xCD,0x32,0x1A,0x3A,0x82,0x20,0x3D, # 0x000004F0 ..@.!@ ...2.:. =
  0xC2,0x08,0x05,0x3E,0x01,0x32,0x6E,0x20,0x2A,0x76,0x20,0xC3,0x7E,0x06,0xE1,0x11, # 0x00000500 .....2n *v .~...
  0x55,0x20,0x3E,0xDB,0xCD,0x50,0x05,0x3A,0x46,0x20,0x32,0x70,0x20,0x3A,0x36,0x20, # 0x00000510 U ...P.:F 2p :6
  0x32,0x71,0x20,0xCD,0x63,0x05,0x3A,0x76,0x20,0xFE,0x15,0xDA,0x34,0x05,0x3A,0x58, # 0x00000520 2q .c.:v ...4.:X
  0x1B,0x32,0x76,0x20,0x3A,0x78,0x20,0xA7,0x21,0x55,0x20,0xC2,0x5B,0x05,0x11,0x50, # 0x00000530 .2v :x .!U .[..P
  0x1B,0x21,0x50,0x20,0x06,0x10,0xCD,0x32,0x1A,0x2A,0x76,0x20,0x22,0x58,0x20,0xC9, # 0x00000540 .!P ...2.*v "X .
  0x32,0x7F,0x20,0x21,0x73,0x20,0x06,0x0B,0xC3,0x32,0x1A,0x11,0x73,0x20,0x06,0x0B, # 0x00000550 2. !s ...2..s ..
  0xC3,0x32,0x1A,0x21,0x73,0x20,0x7E,0xE6,0x80,0xC2,0xC1,0x05,0x3A,0xC1,0x20,0xFE, # 0x00000560 .2.!s ~.....:. .
  0x04,0x3A,0x69,0x20,0xCA,0xB7,0x05,0xA7,0xC8,0x23,0x36,0x00,0x3A,0x70,0x20,0xA7, # 0x00000570 .:i .....#6.:p .
  0xCA,0x89,0x05,0x47,0x3A,0xCF,0x20,0xB8,0xD0,0x3A,0x71,0x20,0xA7,0xCA,0x96,0x05, # 0x00000580 ...G:. ..:q ....
  0x47,0x3A,0xCF,0x20,0xB8,0xD0,0x23,0x7E,0xA7,0xCA,0x1B,0x06,0x2A,0x76,0x20,0x4E, # 0x00000590 G:. ..#~....*v N
  0x23,0x00,0x22,0x76,0x20,0xCD,0x2F,0x06,0xD0,0xCD,0x7A,0x01,0x79,0xC6,0x07,0x67, # 0x000005A0 #."v ./...z.y..g
  0x7D,0xD6,0x0A,0x6F,0x22,0x7B,0x20,0x21,0x73,0x20,0x7E,0xF6,0x80,0x77,0x23,0x34, # 0x000005B0 }..o"{ !s ~..w#4
  0xC9,0x11,0x7C,0x20,0xCD,0x06,0x1A,0xD0,0x23,0x7E,0xE6,0x01,0xC2,0x44,0x06,0x23, # 0x000005C0 ..| ....#~...D.#
  0x34,0xCD,0x75,0x06,0x3A,0x79,0x20,0xC6,0x03,0x21,0x7F,0x20,0xBE,0xDA,0xE2,0x05, # 0x000005D0 4.u.:y ..!. ....
  0xD6,0x0C,0x32,0x79,0x20,0x3A,0x7B,0x20,0x47,0x3A,0x7E,0x20,0x80,0x32,0x7B,0x20, # 0x000005E0 ..2y :{ G:~ .2{
  0xCD,0x6C,0x06,0x3A,0x7B,0x20,0xFE,0x15,0xDA,0x12,0x06,0x3A,0x61,0x20,0xA7,0xC8, # 0x000005F0 .l.:{ .....:a ..
  0x3A,0x7B,0x20,0xFE,0x1E,0xDA,0x12,0x06,0xFE,0x27,0x00,0xD2,0x12,0x06,0x97,0x32, # 0x00000600 :{ ......'.....2
  0x15,0x20,0x3A,0x73,0x20,0xF6,0x01,0x32,0x73,0x20,0xC9,0x3A,0x1B,0x20,0xC6,0x08, # 0x00000610 . :s ..2s .:. ..
  0x67,0xCD,0x6F,0x15,0x79,0xFE,0x0C,0xDA,0xA5,0x05,0x0E,0x0B,0xC3,0xA5,0x05,0x0D, # 0x00000620 g.o.y...........
  0x3A,0x67,0x20,0x67,0x69,0x16,0x05,0x7E,0xA7,0x37,0xC0,0x7D,0xC6,0x0B,0x6F,0x15, # 0x00000630 :g gi..~.7.}..o.
  0xC2,0x37,0x06,0xC9,0x21,0x78,0x20,0x35,0x7E,0xFE,0x03,0xC2,0x67,0x06,0xCD,0x75, # 0x00000640 .7..!x 5~...g..u
  0x06,0x21,0xDC,0x1C,0x22,0x79,0x20,0x21,0x7C,0x20,0x35,0x35,0x2B,0x35,0x35,0x3E, # 0x00000650 .!.."y !| 55+55.
  0x06,0x32,0x7D,0x20,0xC3,0x6C,0x06,0xA7,0xC0,0xC3,0x75,0x06,0x21,0x79,0x20,0xCD, # 0x00000660 .2} .l....u.!y .
  0x3B,0x1A,0xC3,0x91,0x14,0x21,0x79,0x20,0xCD,0x3B,0x1A,0xC3,0x52,0x14,0x22,0x48, # 0x00000670 ;....!y .;..R."H
  0x20,0xC9,0xE1,0x3A,0x80,0x20,0xFE,0x02,0xC0,0x21,0x83,0x20,0x7E,0xA7,0xCA,0x0F, # 0x00000680  ..:. ...!. ~...
  0x05,0x3A,0x56,0x20,0xA7,0xC2,0x0F,0x05,0x23,0x7E,0xA7,0xC2,0xAB,0x06,0x3A,0x82, # 0x00000690 .:V ....#~....:.
  0x20,0xFE,0x08,0xDA,0x0F,0x05,0x36,0x01,0xCD,0x3C,0x07,0x11,0x8A,0x20,0xCD,0x06, # 0x000006A0  .....6...... ..
  0x1A,0xD0,0x21,0x85,0x20,0x7E,0xA7,0xC2,0xD6,0x06,0x21,0x8A,0x20,0x7E,0x23,0x23, # 0x000006B0 ..!. ~....!. ~##
  0x86,0x32,0x8A,0x20,0xCD,0x3C,0x07,0x21,0x8A,0x20,0x7E,0xFE,0x28,0xDA,0xF9,0x06, # 0x000006C0 .2. ...!. ~.(...
  0xFE,0xE1,0xD2,0xF9,0x06,0xC9,0x06,0xFE,0xCD,0xDC,0x19,0x23,0x35,0x7E,0xFE,0x1F, # 0x000006D0 ...........#5~..
  0xCA,0x4B,0x07,0xFE,0x18,0xCA,0x0C,0x07,0xA7,0xC0,0x06,0xEF,0x21,0x98,0x20,0x7E, # 0x000006E0 .K..........!. ~
  0xA0,0x77,0xE6,0x20,0xD3,0x05,0x00,0x00,0x00,0xCD,0x42,0x07,0xCD,0xCB,0x14,0x21, # 0x000006F0 .w. ......B....!
  0x83,0x20,0x06,0x0A,0xCD,0x5F,0x07,0x06,0xFE,0xC3,0xDC,0x19,0x3E,0x01,0x32,0xF1, # 0x00000700 . ..._........2.
  0x20,0x2A,0x8D,0x20,0x46,0x0E,0x04,0x21,0x50,0x1D,0x11,0x4C,0x1D,0x1A,0xB8,0xCA, # 0x00000710  *. F..!P..L....
  0x28,0x07,0x23,0x13,0x0D,0xC2,0x1D,0x07,0x7E,0x32,0x87,0x20,0x26,0x00,0x68,0x29, # 0x00000720 (.#.....~2. &.h)
  0x29,0x29,0x29,0x22,0xF2,0x20,0xCD,0x42,0x07,0xC3,0xF1,0x08,0xCD,0x42,0x07,0xC3, # 0x00000730 )))". .B.....B..
  0x39,0x14,0x21,0x87,0x20,0xCD,0x3B,0x1A,0xC3,0x47,0x1A,0x06,0x10,0x21,0x98,0x20, # 0x00000740 9.!. .;..G...!.
  0x7E,0xB0,0x77,0xCD,0x70,0x17,0x21,0x7C,0x1D,0x22,0x87,0x20,0xC3,0x3C,0x07,0x11, # 0x00000750 ~.w.p.!|.". ....
  0x83,0x1B,0xC3,0x32,0x1A,0x3E,0x01,0x32,0x93,0x20,0x31,0x00,0x24,0xFB,0xCD,0x79, # 0x00000760 ...2...2. 1.$..y
  0x19,0xCD,0xD6,0x09,0x21,0x13,0x30,0x11,0xF3,0x1F,0x0E,0x04,0xCD,0xF3,0x08,0x3A, # 0x00000770 ....!.0........:
  0xEB,0x20,0x3D,0x21,0x10,0x28,0x0E,0x14,0xC2,0x57,0x08,0x11,0xCF,0x1A,0xCD,0xF3, # 0x00000780 . =!.(...W......
  0x08,0xDB,0x01,0xE6,0x04,0xCA,0x7F,0x07,0x06,0x99,0xAF,0x32,0xCE,0x20,0x3A,0xEB, # 0x00000790 ...........2. :.
  0x20,0x80,0x27,0x32,0xEB,0x20,0xCD,0x47,0x19,0x21,0x00,0x00,0x22,0xF8,0x20,0x22, # 0x000007A0  .'2. .G.!..". "
  0xFC,0x20,0xCD,0x25,0x19,0xCD,0x2B,0x19,0xCD,0xD7,0x19,0x21,0x01,0x01,0x7C,0x32, # 0x000007B0 . .%..+....!..|2
  0xEF,0x20,0x22,0xE7,0x20,0x22,0xE5,0x20,0xCD,0x56,0x19,0xCD,0xEF,0x01,0xCD,0xF5, # 0x000007C0 . ". ". .V......
  0x01,0xCD,0xD1,0x08,0x32,0xFF,0x21,0x32,0xFF,0x22,0xCD,0xD7,0x00,0xAF,0x32,0xFE, # 0x000007D0 ....2.!2."....2.
  0x21,0x32,0xFE,0x22,0xCD,0xC0,0x01,0xCD,0x04,0x19,0x21,0x78,0x38,0x22,0xFC,0x21, # 0x000007E0 !2."......!x8".!
  0x22,0xFC,0x22,0xCD,0xE4,0x01,0xCD,0x7F,0x1A,0xCD,0x8D,0x08,0xCD,0xD6,0x09,0x00]

  def __init__(self):
    f=open("threadingMaybeBetter.txt","a+")
    start = int(round(time.time() * 1000))
    thread1 = threading.Thread(target=Disassemble.run, args=(self,)).start()
    threading.Thread.join(self)
    end = int(round(time.time() * 1000))
    f.write(str(end-start) + "\n")

  def run(self):
      while Disassemble.pc < len(Disassemble.instructions):
          Disassemble.interpet(self, hex(Disassemble.instructions[Disassemble.pc]))
          Disassemble.pc += 1

  def interpet(self,hexInstr):
    if(hexInstr == "0x0"):
      print("0x00 NOP")
    elif(hexInstr == "0x1"):
      print("")
      Disassemble.pc+=2
    elif(hexInstr == "0x2"):
      print("")
    elif(hexInstr == "0x3"):
      print("")
    elif(hexInstr == "0x4"):
      print("")
    elif(hexInstr == "0x5"):
      print("")
    elif(hexInstr == "0x6"):
      print("")
      Disassemble.pc+=1
    elif(hexInstr == "0x7"):
      print("")
    elif(hexInstr == "0x8"):
      print("")
    elif(hexInstr == "0x9"):
      print("")
    elif(hexInstr == "0xa"):
      print("")
    elif(hexInstr == "0xb"):
      print("")
    elif(hexInstr == "0xc"):
      print("")
    elif(hexInstr == "0xd"):
      print("")
    elif(hexInstr == "0xe"):
      print("")
      Disassemble.pc+=1
    elif (hexInstr == "0xf"):
      print("")
    elif(hexInstr == "0x10"):
      print()
    elif(hexInstr == "0x11"):
      print()
      Disassemble.pc+=2
    elif(hexInstr == "0x12"):
      print()
    elif(hexInstr == "0x13"):
      print()
    elif(hexInstr == "0x14"):
      print()
    elif(hexInstr == "0x15"):
      print()
    elif(hexInstr == "0x16"):
      print()
      Disassemble.pc+=1
    elif(hexInstr == "0x17"):
      print()
    elif(hexInstr == "0x18"):
      print()
    elif(hexInstr == "0x19"):
      print()
    elif(hexInstr == "0x1a"):
      print()
    elif(hexInstr == "0x1b"):
      print()
    elif(hexInstr == "0x1c"):
      print()
    elif(hexInstr == "0x1d"):
      print()
    elif(hexInstr == "0x1e"):
      print()
      Disassemble.pc+=1
    elif(hexInstr == "0x1f"):
      print()
    elif(hexInstr == "0x20"):
      print()
    elif(hexInstr == "0x21"):
      print()
      Disassemble.pc+=2
    elif(hexInstr == "0x22"):
      print()
      Disassemble.pc+=2
    elif(hexInstr == "0x23"):
      print()
    elif(hexInstr == "0x24"):
      print()
    elif(hexInstr == "0x25"):
      print()
    elif(hexInstr == "0x26"):
      print()
      Disassemble.pc+=1
    elif(hexInstr == "0x27"):
      print()
    elif(hexInstr == "0x28"):
      print()
    elif(hexInstr == "0x29"):
      print()
    elif(hexInstr == "0x2a"):
      print()
      Disassemble.pc+=2
    elif(hexInstr == "0x2b"):
      print()
    elif(hexInstr == "0x2c"):
      print()
    elif(hexInstr == "0x2d"):
      print()
    elif(hexInstr == "0x2e"):
      print()
      Disassemble.pc+=1
    elif(hexInstr == "0x2f"):
      print()
    elif(hexInstr == "0x30"):
      print()
    elif(hexInstr == "0x31"):
      print()
      Disassemble.pc+=2
    elif(hexInstr == "0x32"):
      print()
      Disassemble.pc+=2
    elif(hexInstr == "0x33"):
      print()
    elif(hexInstr == "0x34"):
      print()
    elif(hexInstr == "0x35"):
      print()
    elif(hexInstr == "0x36"):
      print()
      Disassemble.pc+=1
    elif(hexInstr == "0x37"):
      print()
    elif(hexInstr == "0x38"):
      print()
    elif(hexInstr == "0x39"):
      print()
      Disassemble.pc+=2
    elif(hexInstr == "0x3a"):
      print()
    elif(hexInstr == "0x3b"):
      print()
    elif(hexInstr == "0x3c"):
      print()
    elif(hexInstr == "0x3d"):
      print()
    elif(hexInstr == "0x3e"):
      print()
      Disassemble.pc+=1
    elif(hexInstr == "0x3f"):
      print()
    elif(hexInstr == "0x40"):
      print()
    elif(hexInstr == "0x41"):
      print()
    elif(hexInstr == "0x42"):
      print()
    elif(hexInstr == "0x43"):
      print()
    elif(hexInstr == "0x44"):
      print()
    elif(hexInstr == "0x45"):
      print()
    elif(hexInstr == "0x46"):
      print()
    elif(hexInstr == "0x47"):
      print()
    elif(hexInstr == "0x48"):
      print()
    elif(hexInstr == "0x49"):
      print()
    elif(hexInstr == "0x4a"):
      print()
    elif(hexInstr == "0x4b"):
      print()
    elif(hexInstr == "0x4c"):
      print()
    elif(hexInstr == "0x4d"):
      print()
    elif(hexInstr == "0x4e"):
      print()
    elif(hexInstr == "0x4f"):
      print()
    elif(hexInstr == "0x50"):
      print()
    elif(hexInstr == "0x51"):
      print()
    elif(hexInstr == "0x52"):
      print()
    elif(hexInstr == "0x53"):
      print()
    elif(hexInstr == "0x54"):
      print()
    elif(hexInstr == "0x55"):
      print()
    elif(hexInstr == "0x56"):
      print()
    elif(hexInstr == "0x57"):
      print()
    elif(hexInstr == "0x58"):
      print()
    elif(hexInstr == "0x59"):
      print()
    elif(hexInstr == "0x5a"):
      print()
    elif(hexInstr == "0x5b"):
      print()
    elif(hexInstr == "0x5c"):
      print()
    elif(hexInstr == "0x5d"):
      print()
    elif(hexInstr == "0x5e"):
      print()
    elif(hexInstr == "0x5f"):
      print()
    elif(hexInstr == "0x60"):
      print()
    elif(hexInstr == "0x61"):
      print()
    elif(hexInstr == "0x62"):
      print()
    elif(hexInstr == "0x63"):
      print()
    elif(hexInstr == "0x64"):
      print()
    elif(hexInstr == "0x65"):
      print()
    elif(hexInstr == "0x66"):
      print()
    elif(hexInstr == "0x67"):
      print()
    elif(hexInstr == "0x68"):
      print()
    elif(hexInstr == "0x69"):
      print()
    elif(hexInstr == "0x6a"):
      print()
    elif(hexInstr == "0x6b"):
      print()
    elif(hexInstr == "0x6c"):
      print()
    elif(hexInstr == "0x6d"):
      print()
    elif(hexInstr == "0x6e"):
      print()
    elif(hexInstr == "0x6f"):
      print()
    elif(hexInstr == "0x70"):
      print()
    elif(hexInstr == "0x71"):
      print()
    elif(hexInstr == "0x72"):
      print()
    elif(hexInstr == "0x73"):
      print()
    elif(hexInstr == "0x74"):
      print()
    elif(hexInstr == "0x75"):
      print()
    elif(hexInstr == "0x76"):
      print()
    elif(hexInstr == "0x77"):
      print()
    elif(hexInstr == "0x78"):
      print()
    elif(hexInstr == "0x79"):
      print()
    elif(hexInstr == "0x7a"):
      print()
    elif(hexInstr == "0x7b"):
      print()
    elif(hexInstr == "0x7c"):
      print()
    elif(hexInstr == "0x7d"):
      print()
    elif(hexInstr == "0x7e"):
      print()
    elif(hexInstr == "0x7f"):
      print()
    elif(hexInstr == "0x80"):
      print()
    elif(hexInstr == "0x81"):
      print()
    elif(hexInstr == "0x82"):
      print()
    elif(hexInstr == "0x83"):
      print()
    elif(hexInstr == "0x84"):
      print()
    elif(hexInstr == "0x85"):
      print()
    elif(hexInstr == "0x86"):
      print()
    elif(hexInstr == "0x87"):
      print()
    elif(hexInstr == "0x88"):
      print()
    elif(hexInstr == "0x89"):
      print()
    elif(hexInstr == "0x8a"):
      print()
    elif(hexInstr == "0x8b"):
      print()
    elif(hexInstr == "0x8c"):
      print()
    elif(hexInstr == "0x8d"):
      print()
    elif(hexInstr == "0x8e"):
      print()
    elif(hexInstr == "0x8f"):
      print()
    elif(hexInstr == "0x90"):
      print()
    elif(hexInstr == "0x91"):
      print()
    elif(hexInstr == "0x92"):
      print()
    elif(hexInstr == "0x93"):
      print()
    elif(hexInstr == "0x94"):
      print()
    elif(hexInstr == "0x95"):
      print()
    elif(hexInstr == "0x96"):
      print()
    elif(hexInstr == "0x97"):
      print()
    elif(hexInstr == "0x98"):
      print()
    elif(hexInstr == "0x99"):
      print()
    elif(hexInstr == "0x9a"):
      print()
    elif(hexInstr == "0x9b"):
      print()
    elif(hexInstr == "0x9c"):
      print()
    elif(hexInstr == "0x9d"):
      print()
    elif(hexInstr == "0x9e"):
      print()
    elif(hexInstr == "0x9f"):
      print()
    elif(hexInstr == "0xa0"):
      print()
    elif(hexInstr == "0xa1"):
      print()
    elif(hexInstr == "0xa2"):
      print()
    elif(hexInstr == "0xa3"):
      print()
    elif(hexInstr == "0xa4"):
      print()
    elif(hexInstr == "0xa5"):
      print()
    elif(hexInstr == "0xa6"):
      print()
    elif(hexInstr == "0xa7"):
      print()
    elif(hexInstr == "0xa8"):
      print()
    elif(hexInstr == "0xa9"):
      print()
    elif(hexInstr == "0xaa"):
      print()
    elif(hexInstr == "0xab"):
      print()
    elif(hexInstr == "0xac"):
      print()
    elif(hexInstr == "0xad"):
      print()
    elif(hexInstr == "0xae"):
      print()
    elif(hexInstr == "0xaf"):
      print()
    elif(hexInstr == "0xb0"):
      print()
    elif(hexInstr == "0xb1"):
      print()
    elif(hexInstr == "0xb2"):
      print()
    elif(hexInstr == "0xb3"):
      print()
    elif(hexInstr == "0xb4"):
      print()
    elif(hexInstr == "0xb5"):
      print()
    elif(hexInstr == "0xb6"):
      print()
    elif(hexInstr == "0xb7"):
      print()
    elif(hexInstr == "0xb8"):
      print()
    elif(hexInstr == "0xb9"):
      print()
    elif(hexInstr == "0xba"):
      print()
    elif(hexInstr == "0xbb"):
      print()
    elif(hexInstr == "0xbc"):
      print()
    elif(hexInstr == "0xbd"):
      print()
    elif(hexInstr == "0xbe"):
      print()
    elif(hexInstr == "0xbf"):
      print()
    elif(hexInstr == "0xc0"):
      print()
    elif(hexInstr == "0xc1"):
      print()
    elif(hexInstr == "0xc2"):
      print()
      Disassemble.pc+=2
    elif(hexInstr == "0xc3"):
      print()
      Disassemble.pc+=2
    elif(hexInstr == "0xc4"):
      print()
      Disassemble.pc+=2
    elif(hexInstr == "0xc5"):
      print()
    elif(hexInstr == "0xc6"):
      print()
      Disassemble.pc+=1
    elif(hexInstr == "0xc7"):
      print()
    elif(hexInstr == "0xc8"):
      print()
    elif(hexInstr == "0xc9"):
      print()
    elif(hexInstr == "0xca"):
      print()
      Disassemble.pc+=2
    elif(hexInstr == "0xcb"):
      print()
    elif(hexInstr == "0xcc"):
      print()
      Disassemble.pc+=2
    elif(hexInstr == "0xcd"):
      print()
      Disassemble.pc+=2
    elif(hexInstr == "0xce"):
      print()
      Disassemble.pc+=1
    elif(hexInstr == "0xcf"):
      print()
    elif(hexInstr == "0xd0"):
      print()
    elif(hexInstr == "0xd1"):
      print()
    elif(hexInstr == "0xd2"):
      print()
      Disassemble.pc+=2
    elif(hexInstr == "0xd3"):
      print()
      Disassemble.pc+=1
    elif(hexInstr == "0xd4"):
      print()
      Disassemble.pc+=2
    elif(hexInstr == "0xd5"):
      print()
    elif(hexInstr == "0xd6"):
      print()
      Disassemble.pc+=1
    elif(hexInstr == "0xd7"):
      print()
    elif(hexInstr == "0xd8"):
      print()
    elif(hexInstr == "0xd9"):
      print()
    elif(hexInstr == "0xda"):
      print()
      Disassemble.pc+=2
    elif(hexInstr == "0xdb"):
      print()
      Disassemble.pc+=1
    elif(hexInstr == "0xdc"):
      print()
      Disassemble.pc+=2
    elif(hexInstr == "0xdd"):
      print()
    elif(hexInstr == "0xde"):
      print()
      Disassemble.pc+=1
    elif(hexInstr == "0xdf"):
      print()
    elif(hexInstr == "0xe0"):
      print()
    elif(hexInstr == "0xe1"):
      print()
    elif(hexInstr == "0xe2"):
      print()
      Disassemble.pc+=2
    elif(hexInstr == "0xe3"):
      print()
    elif(hexInstr == "0xe4"):
      print()
      Disassemble.pc+=2
    elif(hexInstr == "0xe5"):
      print()
    elif(hexInstr == "0xe6"):
      print()
      Disassemble.pc+=1
    elif(hexInstr == "0xe7"):
      print()
    elif(hexInstr == "0xe8"):
      print()
    elif(hexInstr == "0xe9"):
      print()
    elif(hexInstr == "0xea"):
      print()
      Disassemble.pc+=2
    elif(hexInstr == "0xeb"):
      print()
    elif(hexInstr == "0xec"):
      print()
      Disassemble.pc+=2
    elif(hexInstr == "0xed"):
      print()
    elif(hexInstr == "0xee"):
      print()
      Disassemble.pc+=1
    elif(hexInstr == "0xef"):
      print()
    elif(hexInstr == "0xf0"):
      print()
    elif(hexInstr == "0xf1"):
      print()
    elif(hexInstr == "0xf2"):
      print()
      Disassemble.pc+=2
    elif(hexInstr == "0xf3"):
      print()
    elif(hexInstr == "0xf4"):
      print()
      Disassemble.pc+=2
    elif(hexInstr == "0xf5"):
      print()
    elif(hexInstr == "0xf6"):
      print()
      Disassemble.pc+=1
    elif(hexInstr == "0xf7"):
      print()
    elif(hexInstr == "0xf8"):
      print()
    elif(hexInstr == "0xf9"):
      print()
    elif(hexInstr == "0xfa"):
      print()
      Disassemble.pc+=2
    elif(hexInstr == "0xfb"):
      print()
    elif(hexInstr == "0xfc"):
      print()
      Disassemble.pc+=2
    elif(hexInstr == "0xfd"):
      print()
    elif(hexInstr == "0xfe"):
      print()
      Disassemble.pc+=1
    elif(hexInstr == "0xff"):
      print()
def main():
    Dis = Disassemble()


main()