# export REPLICATE_API_TOKEN = "r8_AGiMSjEEXyJIAcH3dvmJSwQ0mmCR4ON0zvpq1"
import replicate

output = replicate.run(
    "pharmapsychotic/clip-interrogator:a4a8bafd6089e1716b06057c42b19378250d008b80fe87caa5cd36d40c1eda90",
    input={"image": open("Multichannel/loops/Animals.png", "rb"), "clip_model_name": "ViT-H-14/laion2b_s32b_b79k", "mode": "fast"}
)
print(output)