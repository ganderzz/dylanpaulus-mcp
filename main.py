import os
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Dylan Paulus MCP")

POSTS_PATH = os.path.join("..", "dylanpaulus.com", "src", "content", "post")


@mcp.tool()
def get_posts() -> str:
    """Get all posts"""
    contents = []
    directories = [f.path for f in os.scandir(POSTS_PATH) if f.is_dir()]
    for directory in directories:
        path = os.path.join(directory, "index.mdx")
        if not os.path.isfile(path):
            continue
        with open(path) as file:
            contents.append(file.read())

    return contents


@mcp.tool()
def get_post(post_name: str) -> str:
    """Get a specific post"""
    path = os.path.join(str(POSTS_PATH), post_name, "index.mdx")
    if os.path.isfile(path):
        with open(path) as file:
            return file.read()

    raise ValueError(
        f"Invalid post_name {post_name} given.\nEither the `index.mdx` file is missing or this directory does not exist ({path})."
    )


if __name__ == "__main__":
    mcp.run(transport="stdio")
