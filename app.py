import gradio as gr
import subprocess
import os


def download_audio(video_links, quality_priority, download_path):
    if (
        not video_links.strip()
        or not quality_priority.strip()
        or not download_path.strip()
    ):
        return "输入不能为空"

    for video_link in video_links.split("\n"):
        video_link = video_link.strip()
        if video_link:
            command = [
                "BBDown",
                f"--ffmpeg-path=D:\\ffmpeg\\ffmpeg-master-latest-win64-gpl\\ffmpeg-master-latest-win64-gpl\\bin\\ffmpeg.exe",
                f"--work-dir={download_path}",
                f"--dfn-priority={quality_priority}",
                video_link,
            ]
            try:
                # Start the subprocess
                process = subprocess.Popen(
                    command,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    bufsize=1,  # Line-buffered
                )

                # Read outputs in real-time
                for line in process.stdout:
                    yield f"[输出] {line.strip()}"

                # Wait for the process to complete and capture any remaining output
                process.wait()
                if process.returncode == 0:
                    yield f"下载成功：{video_link}"
                else:
                    stderr_output = process.stderr.read().strip()
                    yield f"下载失败({video_link})：{stderr_output}"

            except FileNotFoundError:
                yield "找不到 BBDown 或 ffmpeg 工具"
                break
            except Exception as e:
                yield f"发生未知错误({video_link})：{str(e)}"
                break


iface = gr.Interface(
    fn=download_audio,
    inputs=[
        gr.Textbox(label="Bilibili 视频链接（每行一个链接）"),
        gr.Textbox(
            label="音频质量优先级（例如：1080P 高码率, 720P 高码率）",
            placeholder="1080P 高码率, 720P 高码率",
        ),
        gr.Textbox(label="下载路径", placeholder="E:\\AudioDownloads"),
    ],
    outputs="text",
    title="Bilibili 视频频下载器",
    description="输入Bilibili视频链接，选择音频质量，并指定下载路径以下载视频音频。支持一次下载多个链接。",
    theme="default",
    css="""footer.svelte-1rjryqp { display: none !important; }""",
)

iface.launch(share=True)
