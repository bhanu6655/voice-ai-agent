let mediaRecorder;

let audioChunks = [];

async function startRecording() {

    document.getElementById("status").innerText =
        "Recording...";

    const stream =
        await navigator.mediaDevices.getUserMedia({
            audio: true
        });

    mediaRecorder = new MediaRecorder(stream);

    mediaRecorder.start();

    audioChunks = [];

    mediaRecorder.ondataavailable = event => {
        audioChunks.push(event.data);
    };

    setTimeout(() => {

        mediaRecorder.stop();

    }, 5000);

    mediaRecorder.onstop = async () => {

        const audioBlob =
            new Blob(audioChunks, {
                type: 'audio/wav'
            });

        const formData = new FormData();

        formData.append(
            "audio",
            audioBlob,
            "input.wav"
        );

        const response = await fetch("/voice", {
            method: "POST",
            body: formData
        });

        const audioResponse = await response.blob();

        const audioURL =
            URL.createObjectURL(audioResponse);

        const audioPlayer =
            document.getElementById("audioPlayer");

        audioPlayer.src = audioURL;

        audioPlayer.play();

        document.getElementById("status").innerText =
            "Response received";
    };
}