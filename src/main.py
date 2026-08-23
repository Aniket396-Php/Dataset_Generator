import sys

from src.logger import logger

from src.generator import DatasetGenerator

def main():
    try:
        generator = DatasetGenerator()
        generator.run()
    except KeyboardInterrupt:
        logger.info("Generation interrupted by user.")
        print("\nGeneration interrupted by user. Saved checkpoint.")
        sys.exit(0)
    except Exception as e:
        logger.critical(f"Fatal error: {str(e)}")
        print(f"\nFatal error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
