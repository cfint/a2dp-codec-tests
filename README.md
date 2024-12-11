
# Testing the performance of A2DP sink audio codecs on ESP32

This documents a procedure for testing the performance of A2DP sink audio codecs on ESP32. The tests are peformed with minimal hardware costs. No expensive audiophile equipment is used.

## Hardware

- ESP32-CAM module
- PCM5102A module
- 3.5mm male-to-male cable
- PC or Laptop with 3.5mm audio input

## Software

- Arch Linux
- Audacity
- `aplay`
- python: pandas, matplotlib

## Test Procedure

Build a bluetooth speaker using ESP32 and PCM5102A modules. Flash a2dp sink to ESP32 module. Connect 3.5mm cable from PCM5102A module to PC 3.5mm input.

Generate test audio files unsing Audacity. Use `aplay` to playback audio files. Avoid frontend audio players like VLC which may have post processing effects enabled. At least make sure they are disabled if you must those players.

Select an A2DP codec with your desktop environment sound settings.

Play the audio file while recording line-in with Audacity. Export the audio spectrum to CSV file. `Analyze` > `Plot Spectrum...` > `Export`

Audacity FFT settings:

    Function: Hamming Window
    Size: 131072

Use `plot_spectrum.py --file spectrum.txt` to generate an image of the frequency spectrum.

Compare the frequency spectrum of audio to codecs to the original audio file. Compare the frequency spectrum of audio codecs to each other.


## Generating test audio in Audacity

1. Generate a 1 minute long 1khz tone
2. `Tools` > `Nyquist Prompt`
3. Use Nyquist prompts below to generate test audio files.

Cookie Bite:

    (sim
        (scale 0.2 (hzosc 250))
        (scale 0.2 (hzosc 500))
        (scale 0.2 (hzosc 1000))
        (scale 0.2 (hzosc 2000))
        (scale 0.2 (hzosc 4000))
        (scale 0.2 (hzosc 8000))
    )

Multi-tone

    (sim
        (scale 0.2 (hzosc 100))
        (scale 0.2 (hzosc 1000))
        (scale 0.2 (hzosc 5000))
        (scale 0.2 (hzosc 10000))
        (scale 0.2 (hzosc 15000))
    )

Multi-tone 20

    (sim
        (scale 0.2 (hzosc 20))
        (scale 0.2 (hzosc 200))
        (scale 0.2 (hzosc 500))
        (scale 0.2 (hzosc 1000))
        (scale 0.2 (hzosc 2000))
        (scale 0.2 (hzosc 3000))
        (scale 0.2 (hzosc 4000))
        (scale 0.2 (hzosc 5000))
        (scale 0.2 (hzosc 6000))
        (scale 0.2 (hzosc 7000))
        (scale 0.2 (hzosc 8000))
        (scale 0.2 (hzosc 9000))
        (scale 0.2 (hzosc 10000))
        (scale 0.2 (hzosc 11000))
        (scale 0.2 (hzosc 12000))
        (scale 0.2 (hzosc 13000))
        (scale 0.2 (hzosc 14000))
        (scale 0.2 (hzosc 15000))
        (scale 0.2 (hzosc 16000))
        (scale 0.2 (hzosc 17000))
    )


## Comments

This is mainly testing playback from Linux (pipewire). Actual Bluetooth hardware A2DP sources may (or may not) have different performance.

The Cookie Bite test sample is intended to test approximately the frequency range of speech (250hz to 8000hz).

The Apple AAC encoder appears to be the highest quality codec. No exceptions. The AAC encoder on Linux (fdk-aac) appears to be very low quality. Worse than SBC.

The LDAC codec in High Quality mode (hq 990/909kbps) is quite good. Quality drops off rapidly in Standard Quality (sq 660/606kbps) and Mobile Quality (mq 330/303kbps).

The more recent implementation of the LDAC decoder (O2C14/libldac-dec) has slightly less noise then the first implementation (hegdi/libldacdec).

The aptX codec has a very high noise floor. Especially in the higher frequency ranges. It's uncertain if this is an issue with the encoder and/or decoder. Perhaps some other aptX source devices may provide better results.

The Opus05 and lc3plus-hr codecs are an invention of Pipewire. These codecs appear to be just okay. Nothing remarkable or terrible.
