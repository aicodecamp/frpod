const player = videojs("myvideo", {
  autoplay: "muted",
  controls: true,
  //poster: ''
  //   loop: true,
  //fluid, aspectRatio,
  //   playbackRates: [0.25, 0.5, 1, 1.5],
  // plugins: {
  //   hotkeys: {
  //     volumeStep: 0.1,
  //     seekStep: 5,
  //     enableModifiersForNumbers: false,
  //   },
  // },
});
/*
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
*/

const tracks = player.textTracks();
const track0 = tracks[0];
console.log(" tracks = ", tracks);
console.log(" track0 = ", track0);
var aTextTrack = player.textTracks()[0];
console.aTextTrack.on("loaded", function () {
  console.log("here it is");
  cues = aTextTrack.cues();
  console.log("Ready State", aTextTrack.readyState());
  console.log("Cues", cues);
});

aTextTrack.show(); //this method call triggers the subtitles to be loaded and loaded trigger

// Play through the playlist automatically.
player.playlist.autoadvance(0);

// rotate
player.rotate(player);

// player.playbackRate(1);
// player.currentTime(1);

player.pause();
player.play();

console.log("start playing...");
