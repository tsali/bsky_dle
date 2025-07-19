# bsky_dle
a python script to download media you've posted to bluesky

Q: Can you download anyones images and videos?
A: Yes. Should you though? Probably not, that's their content and they own it, don't abuse this okay? Just use this wisely to keep a back-up of your content in case you didn't save it or you lost your phone or PC or what-have-you.

Q: How do I get my bearer token?
A: curl -s -X POST "https://bsky.social/xrpc/com.atproto.server.createSession"   -H "Content-Type: application/json"   -d '{"identifier":"YOURBLUESKYHANDLE","password":"YOURPASSWORD"}' | jq -r '.accessJwt'

Q: Can I make this cleaner?
A: Yeah, probably, but it'll likely die in the pits of being forgotten like everything else I make and then never use again.

Usage

To download the last 5 days media you've posted:

python dle.py YOURUSERNAME 5

To download everything you've posted do the same but without the number of days command line arguement/modifier

python dle.py YOURUERNAME

Real world example:

pi@retropi5:~/bskytest $ python dle.py cultofjames.org 5
📡 Resolving DID for cultofjames.org...
✅ DID: did:plc:lgqsxtzms2ewuiici72azcoh
Downloading:   0%|                                                                                                                                                                                                                         | 0/19 [00:00<?, ?it/s]✅ Image: cultofjames.org/bafkreidvvfod6wi2dy5qpg7vacl7s6dtfdxnxtgyliooqbvqjvcyromzuq.jpeg
Downloading:   5%|███████████                                                                                                                                                                                                      | 1/19 [00:00<00:07,  2.57it/s]✅ Image: cultofjames.org/bafkreigvqgo3al2epymehdtrmp7cmc2gacu6q5tcfruq3w6wthvwy5wzku.jpeg
Downloading:  11%|██████████████████████                                                                                                                                                                                           | 2/19 [00:00<00:06,  2.69it/s]✅ Image: cultofjames.org/bafkreia35ffnsv5mubbjnzpgjbvblqmw6thfsxqdnhwmbzu6ffxqhpeqpq.jpeg
Downloading:  16%|█████████████████████████████████                                                                                                                                                                                | 3/19 [00:01<00:05,  2.89it/s]✅ Image: cultofjames.org/bafkreiau33qkb6worfludgbyoy567fsg2ixwbxoyudig4xuearpsbovlue.jpeg
Downloading:  21%|████████████████████████████████████████████                                                                                                                                                                     | 4/19 [00:01<00:04,  3.01it/s]✅ Image: cultofjames.org/bafkreidvym4dpbovlg4hhscrxvtwiwcdnjbseisxwnye5i6w5kpqyiscni.jpeg
Downloading:  26%|███████████████████████████████████████████████████████                                                                                                                                                          | 5/19 [00:01<00:04,  3.16it/s]✅ Image: cultofjames.org/bafkreiaz7nac3we6hdokinqmg5i5y7qvbfaqbo26v7qgfo3v3mbv3wn5cu.jpeg
Downloading:  32%|██████████████████████████████████████████████████████████████████                                                                                                                                               | 6/19 [00:01<00:03,  3.37it/s]✅ Image: cultofjames.org/bafkreihdjpm42gvcn5tuts6a4izzhwk5qywcmdyc4t6b5mqsgn6bcwxjiu.jpeg
Downloading:  37%|█████████████████████████████████████████████████████████████████████████████                                                                                                                                    | 7/19 [00:02<00:03,  3.23it/s]✅ Image: cultofjames.org/bafkreiduod4j4qqhnv7egwvy62vg7cyaisgrrqfgw6ipz5vzziwwhiz3q4.jpeg
Downloading:  42%|████████████████████████████████████████████████████████████████████████████████████████                                                                                                                         | 8/19 [00:02<00:03,  2.98it/s]✅ Image: cultofjames.org/bafkreieb5whf3n3tygbipxxmnccsyaryk6qqbm2cpniyienqxlvm242veu.jpeg
Downloading:  47%|███████████████████████████████████████████████████████████████████████████████████████████████████                                                                                                              | 9/19 [00:02<00:03,  2.95it/s]✅ Image: cultofjames.org/bafkreie6izn65q6uv4i6e2xsp5rzrkh5yyfjijmnyszfdedex5k6pwjiny.jpeg
Downloading:  53%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████▍                                                                                                  | 10/19 [00:03<00:03,  2.91it/s]✅ Image: cultofjames.org/bafkreidibxb3cdx57pnjfqzalmnmbhgwynmpdmaicty2vkeuzx2utgwxf4.jpeg
Downloading:  58%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▍                                                                                       | 11/19 [00:03<00:02,  2.85it/s]✅ Image: cultofjames.org/bafkreibw2pa72qbap2edi2byzdv7nbbgajahkuf2gze6msfzzd75jbilzy.jpeg
Downloading:  63%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▎                                                                            | 12/19 [00:04<00:02,  3.00it/s]✅ Image: cultofjames.org/bafkreif6crn72gqtgyjpbe3pdfv7oyfkbqkw74xf5sbfqnhtvot7kyoqvu.jpeg
Downloading:  68%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▎                                                                 | 13/19 [00:04<00:02,  2.84it/s]✅ Image: cultofjames.org/bafkreie25xbc7wzrhwql6ce4c25a72iad2udjkbkziie3nkzfuoc7zuffe.jpeg
Downloading:  74%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▎                                                      | 14/19 [00:04<00:01,  2.79it/s]✅ Image: cultofjames.org/bafkreifojgezitdtz4zz5uwjztrqdsksnyvq4g2wunkcfpj2ideeu4qoky.jpeg
Downloading:  79%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▏                                           | 15/19 [00:05<00:01,  2.72it/s]✅ Image: cultofjames.org/bafkreia6sbetkk7lkv25zzs2nb6pwgjtksb7e5k7ubfreq3cpykictah3m.jpeg
Downloading:  84%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▏                                | 16/19 [00:05<00:01,  2.69it/s]✅ Image: cultofjames.org/bafkreibqklbl4ldfi3kt65usjznizpn7dozcmpulerhtlb6houtbiltdpq.jpeg
Downloading:  89%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████                      | 17/19 [00:05<00:00,  2.74it/s]✅ Image: cultofjames.org/bafkreie25scpi6u6f3htrza7rkzgmt6k3rpb33jlay332ca6fkpmjaeaee.jpeg
Downloading:  95%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████           | 18/19 [00:06<00:00,  2.93it/s]✅ Image: cultofjames.org/bafkreihaik7gmlfwbi67iyfih3gba3tlzbu3ssix7acupvodvpzxnkwoeq.jpeg
Downloading: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 19/19 [00:06<00:00,  2.91it/s]
Downloading: 0it [00:00, ?it/s]
Downloading: 0it [00:00, ?it/s]
Downloading: 0it [00:00, ?it/s]
Downloading: 0it [00:00, ?it/s]
Downloading: 0it [00:00, ?it/s]
Downloading: 0it [00:00, ?it/s]
Downloading: 0it [00:00, ?it/s]
Downloading: 0it [00:00, ?it/s]
Downloading: 0it [00:00, ?it/s]
Downloading: 0it [00:00, ?it/s]
Downloading: 0it [00:00, ?it/s]
Downloading: 0it [00:00, ?it/s]
🏁 Done.
