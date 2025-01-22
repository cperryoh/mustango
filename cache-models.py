from huggingface_hub import snapshot_download
import os

def cache_model():
    try:
        print("Downloading and caching Riffusion model...")
        cache_dir = "/workspace/models"
        os.makedirs(cache_dir, exist_ok=True)

        # Download the riffusion model
        snapshot_download(
            "declare-lab/mustango",
            local_dir=cache_dir,
            local_dir_use_symlinks=False,
            repo_type="model"
        )

        print("Model successfully cached")
        return True
    except Exception as e:
        print(f"Model caching failed: {str(e)}")
        return False

if __name__ == "__main__":
    success = cache_model()
    exit(0 if success else 1)
