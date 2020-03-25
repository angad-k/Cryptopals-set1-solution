# Cryptopals-set1-solution

- **Challenge 1**<br>
  The code is pretty self explanatory. Used unhexlify to get the byte array or the byte sequence and then encoded it in base64.<br>
- **Challenge 2**<br>
  The comments for the code in this explain everything. Got the byte array from the hex strings and then XORd them to get the resultant string<br>
- **Challenge 3**<br>
  <del>Okay, first of all, please forgive me for that absolutely terrible if-else tree that I have used in this code and maybe in some other consecutive codes. Wasnt't comfortable with python at the time of coding it leading to that absolutely ugly abomination.</del> Fixed it! Yipee!<br>
  So, yeah. I have used the scorer for scoring the strings according to a frequency chart that I found online.  We basically brute force our ways through all possible ASCII characters before outputting the 11 most probable answers.<br>
- **Challenge 4**<br>
  So, here I put all strings through a brute force single-byte XOR and ranked them according to the scores from frequency of top 10 strings. In this way, I shortlisted top 10 most probable strings which are stored in <i>shortlistchall3</i>. Put these strings through the code for previous program to get the actual string.
- **Challenge 5**<br>
  The code for this is pretty self explanatory.
- **Challenge 6**<br>
  Okay, this one, I have broken into two parts. The first part is mostly to narrow down on keysize. Most of the part is commented, so I'll explain the final step from part 1. All the most probable strings were stored in <i>bestStrR(keysize).txt</i> Out of all of them, bestStrR29.txt showed the maximum semblence to English, Howver, it wasn't yet perfect. <br>
  Here's where part 2 comes in. Now, I knew the keysize. All I wanted to do is perfect the output. So, why wasn't it perfect already? Welll, that's because, it might be that the rank of the correct key value might be a little below according to the frequency chart. So, in part2, I slowly tweaked the code, so we use the second most probable and in some cases, the third most probable key value to be used. This sounds tedious, but isn't. Because for the first 29 characters correspond to first 29 key choices. I mean, if we change the first key value, first character in the output string will change and so on.
- **Challenge 7** <br>
  Nothing to explain here. :)
- **Challenge 8**<br>
  Well,I'm still not 100% convinced about the coding I've done here. The hint said that EBC is stateless and deterministic. So, the same combination of 16 bytes shall output the same 16 byte output. So, I just counted the reptitions of the same in the output and ranked the strings accordingly. However, I don't understand why the 16 bytes would be repeated in the input in the first place.
