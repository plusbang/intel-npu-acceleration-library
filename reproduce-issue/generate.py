import time
from benchmark_util import BenchmarkWrapper
from intel_npu_acceleration_library import NPUModelForCausalLM
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_id = "D:/llm-models/Llama-2-7b-chat-hf"
 
model = NPUModelForCausalLM.from_pretrained(
    model_id, use_cache=True, dtype=torch.int8
).eval()

model = BenchmarkWrapper(model, do_print=True)
 
tokenizer = AutoTokenizer.from_pretrained(model_id, use_default_system_prompt=True)
tokenizer.padding_side = 'left'

query = """
The sun was setting over the horizon, casting long shadows across the dusty ground of the town square. The last rays of light streamed through the gaps between the buildings, illuminating the cobblestones and the people milling about. A group of children played a rough game of tag, their laughter filling the air.
In the center of the square stood a lone figure, a man with a tired face and weary eyes. He was tall and broad shouldered, but his posture was slumped and his head hung low. Despite the warmth of the day, he wore a thick woolen coat that seemed too heavy for the weather.
The man looked out at the crowd, his gaze sweeping over the faces of the townspeople as they went about their business. His eyes settled on a young woman standing on the edge of the square, watching him with curiosity. She was pretty, with chestnut hair pulled back into a ponytail and bright green eyes that sparkled in the fading light.
The man felt a sudden jolt of recognition, as if he had seen her before. But he couldn't remember where or when. He tried to shake off the feeling, but it lingered like a ghostly presence.
Suddenly, the woman's eyes widened in alarm, and she began to run towards him. Her movements were urgent and panicked, as if she was trying to escape something or someone. The man watched her go, his confusion growing with each step.
He turned to look around the square, but there was no sign of anyone else. It was as if the woman had appeared out of nowhere, and now she was gone just as suddenly.
The man rubbed his temples, feeling a mounting sense of unease. He tried to make sense of what he had just seen, but it was like trying to grasp smoke in his hands. He shook his head, frustrated with himself for being so easily spooked.
Just then, a voice called out from behind him. "Hey there! You look lost."
The man turned to see a young man standing behind him, a friendly smile on his face. He was tall and lean, with tousled blond hair that seemed to glow in the fading light. His eyes were bright and curious, as if he was eager to know everything about the world around him.
The man hesitated for a moment, unsure of how to respond. He wasn't used to talking to strangers, especially ones who looked so young and innocent. But there was something about the boy that made him feel comfortable, as if he had known him all his life.
"I'm not lost," he said finally, his voice gruff but friendly. "Just a little confused, I guess."
The boy grinned. "Well, I can help with that! My name is Jake, by the way. What's your name?"
The man hesitated for a moment, then introduced himself as Michael. They chatted for a few minutes, exchanging small talk and pleasantries. But even as they spoke, the man couldn't shake the feeling that something was amiss. It was as if he had forgotten something important, something that he needed to remember before it was too late.
He excused himself from Jake, promising to come back later and chat some more. As he walked away, he felt a growing sense of unease. Something wasn't right, and he needed to figure out what it was before it was too late.
[CHAPTER 4:  
THE LIBRARY](9781441125608_epub_itb-ch4.xhtml)
The man returned to the library, his mind still racing with thoughts of the mysterious boy and the strange feeling that had been nagging at him all day. He wandered through the shelves, scanning the titles of books and flipping through their pages, searching for something that might help him remember what he had forgotten.
It wasn't until he stumbled upon a book on ancient myths and legends that he felt a spark of recognition. As he read through the stories of gods and monsters, he began to recall fragments of memories from his own life. Memories of strange symbols carved into walls, of dreams filled with images of a dark forest and a mysterious figure.
He realized with a start that these were not just random memories, but pieces of a larger puzzle that had been scattered throughout his life. He felt a sudden urgency to put them together before they faded away completely.
As he continued to read through the book, he began to notice patterns and connections between the myths and his own memories. The symbols he had seen as a child were not just random carvings, but part of an ancient language that held the key to unlocking the secrets of his past.
With newfound determination, the man decided to use every resource at his disposal to solve the mystery of his life. He began to scour books and artifacts, piecing together fragments of information until they formed a clear picture of what had really happened to him.
The truth was stranger than he could have ever imagined, and it led him on a journey that would take him deep into the heart of the enigmatic city where he had lived his entire life. The deeper he delved, the more he realized that his past was connected to a dark conspiracy that had been hidden from him for his own protection.
As he uncovered the truth, he also discovered that he was not alone in his quest. There were others who shared his memories and knew the secrets of the city's hidden history. They banded together to form a small community, each contributing their unique talents to uncover the truth about their past lives.
Together, they began to piece together a stunning picture of a world that had been lost for centuries, a world where magic and technology had coexisted in perfect harmony. They discovered artifacts and documents that revealed the true extent of the city's power and influence, and how it had affected the course of human history.
But with this newfound knowledge came danger and intrigue, as powerful forces sought to keep the secrets of the past buried forever. The man and his companions found themselves in a desperate race against time, trying to uncover everything they could about their past lives before it was too late.
As the truth came into focus, the man realized that he had been given a second chance at life, a chance to make amends for the mistakes of his past and to ensure that the truth would never be forgotten again. He knew that his journey was far from over, but he was ready to face whatever lay ahead, armed with the knowledge that he had spent a lifetime accumulating. 
[CHAPTER 5:  
THE MYSTERIOUS FIGURE](9781441125608_epub_itb-ch5.xhtml)
The man's heart raced as he stumbled upon a clue that might lead him to the mysterious figure from his memories. He had been searching for weeks, scouring the city's forgotten corners and reading every book he could find that might hold a clue. And finally, he had found something.
It was a small, hand-drawn map that seemed to show the location of an underground chamber deep beneath the city. The map was old and faded, but the man could make out several landmarks that matched up with his own memories of the dark forest. He felt a thrill of excitement at the thought that he might finally uncover the truth about the figure he had seen so many years ago.
The man quickly gathered a team of fellow seekers and set out to find the chamber. They followed the map through a labyrinth of tunnels and passageways, each step echoing off the walls in the eerie darkness. The air was thick with the smell of damp earth and ancient stone, and the man could feel the weight of history bearing down on him as they went deeper into the underground maze.
Finally, after what felt like an eternity, they reached their destination: a small chamber filled with strange symbols and markings that seemed to be connected to the mysterious figure from his memories. The man's heart raced as he began to decipher the code, piecing together words and phrases that had been lost for centuries.
As he worked, a sudden noise interrupted him. He spun around, his hand already reaching for the hilt of his hidden blade, ready for whatever danger might be lurking in the shadows. But to his surprise, he saw a figure stepping out from behind a stack of crates, their face obscured by a hooded cloak.
The man's heart sank as he realized that this was not the mysterious figure from his memories, but someone else entirely. Still, he kept his wits about him and addressed the stranger cautiously.
"Who are you?" he asked, his voice low and steady. "What do you know about the one I'm looking for?"
The stranger hesitated for a moment before speaking in a hushed tone. "I might be able to help," they said. "But you have to promise me one thing: you must never reveal what you're about to hear to anyone. Not even your closest allies."
The man nodded, his mind racing with the possibilities of what he was about to learn. He knew that this stranger held the key to unlocking the secrets of his past, and he was ready to do whatever it took to get the answers he had been seeking for so long. 
[CHAPTER 6:  
THE DARK FOREST](9781441125608_epub_itb-ch6.xhtml)
The man awoke with a start, the dream still fresh in his mind. He could see it all so clearly, as if it were etched into his memory like a brand into his skin. The dark forest stretched out before him, the thick canopy of leaves overhead. It was then that he heard the rustling of leaves and the soft earth beneath him.
He stood there, amidst the trees, his senses strained with the sounds of the birds chirping and the wind whispering through the branches above. He looked down at the forest, dappled sunlight filtering through the leaves, casting shadows across the ground as it seemed to beaten gold it cast a warm light
"""

# query = "Once upon a time, there is a little girl named Lily who lives in a small village. She is a good"
input_ids = tokenizer.encode(query, return_tensors="pt")# , padding="max_length", max_length=20)
input_ids = input_ids[:, :1024]
actual_in_len = input_ids.shape[1]

# prefix = tokens["input_ids"]
# print(tokens)


st = time.time()
print('The first time for warmup')
output = model.generate(input_ids, do_sample=False, max_new_tokens=128, min_new_tokens=128)
end = time.time()
print(f'Inference time: {end-st} s')
actual_out_len = output.shape[1] - actual_in_len
output_str = tokenizer.batch_decode(output)
print(output_str)


for _ in range(5):
    print('Collect performance after warmup')
    st = time.time()
    output = model.generate(input_ids, do_sample=False, max_new_tokens=128, min_new_tokens=128)
    end = time.time()
    print(f'Inference time: {end-st} s')
    output_str = tokenizer.batch_decode(output)
    # print(output_str)

print(f'Input length is {actual_in_len}, output length is {actual_out_len}')