const player = videojs("myvideo", {
  autoplay: "muted",
  controls: true,
  //poster: ''
  //   loop: true,
  //fluid, aspectRatio,
  //   playbackRates: [0.25, 0.5, 1, 1.5],
  plugins: {
    hotkeys: {
      volumeStep: 0.1,
      seekStep: 5,
      enableModifiersForNumbers: false,
    },
  },
});

player.playlist([
  {
    sources: [
      {
        src: "http://media.w3.org/2010/05/sintel/trailer.mp4",
        type: "video/mp4",
      },
    ],
    poster: "http://media.w3.org/2010/05/sintel/poster.png",
  },
  {
    sources: [
      {
        src: "http://media.w3.org/2010/05/bunny/trailer.mp4",
        type: "video/mp4",
      },
    ],
    poster: "http://media.w3.org/2010/05/bunny/poster.png",
  },
  {
    sources: [
      {
        src: "http://vjs.zencdn.net/v/oceans.mp4",
        type: "video/mp4",
      },
    ],
    poster: "http://www.videojs.com/img/poster.jpg",
  },
  {
    sources: [
      {
        src: "http://media.w3.org/2010/05/bunny/movie.mp4",
        type: "video/mp4",
      },
    ],
    poster: "http://media.w3.org/2010/05/bunny/poster.png",
  },
  {
    sources: [
      {
        src: "http://media.w3.org/2010/05/video/movie_300.mp4",
        type: "video/mp4",
      },
    ],
    poster: "http://media.w3.org/2010/05/video/poster.png",
  },
]);

// Play through the playlist automatically.
player.playlist.autoadvance(0);

// rotate
player.rotate(player);

player.playbackRate(2);
player.currentTime(1);

player.pause();
player.play();

console.log("start playing...");
