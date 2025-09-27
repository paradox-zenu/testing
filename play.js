// React example
import React, { useEffect, useState } from 'react';

function Play({ videoId }) {
  const [audioUrl, setAudioUrl] = useState('');
  useEffect(() => {
    async function fetchAudio() {
      // Backend endpoint extracts audio from YouTube (using yt-dlp)
      const res = await fetch(`/api/audio/${videoId}`);
      const data = await res.json();
      setAudioUrl(data.audioUrl);
    }
    fetchAudio();
  }, [videoId]);
  
  return (
    <div>
      <h2>Playing Music</h2>
      <audio controls src={audioUrl} autoPlay />
    </div>
  );
}

export default Play;