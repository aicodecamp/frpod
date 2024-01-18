import { translate as externalTranslate } from "deeplx";
// @ts-ignore
//const webvtt = require("node-webvtt");
import * as webvtt from "node-webvtt";
import fs from "fs";
import { promisify } from "util";
// const fs = require("fs");
// const { promisify } = require("util");
// const assert = require("assert");

// // Mock external translation function
// async function externalTranslate(text, targetLanguage, sourceLanguage) {
//   // Replace this with your actual translation logic or API call
//   console.log(
//     `Translating "${text}" from ${sourceLanguage} to ${targetLanguage}`
//   );
//   return `${text} [Translated]`;
// }

const readFileAsync = promisify(fs.readFile);

async function translateParsedVtt(parsed, targetLanguage, sourceLanguage) {
  let i = 0;
  for (; i < parsed.cues.length; i++) {
    const cue = parsed.cues[i];
    const translatedText = await externalTranslate(
      cue.text,
      targetLanguage,
      sourceLanguage
    );
    parsed.cues[i].text = translatedText;
  }
}

async function getTranslatedVttForPathname(
  pathname,
  targetLanguage,
  sourceLanguage
) {
  try {
    const data = await readFileAsync(pathname, "utf-8");
    const parsed = webvtt.parse(data);
    await translateParsedVtt(parsed, targetLanguage, sourceLanguage);
    return webvtt.compile(parsed);
  } catch (error) {
    console.error(`Error translating WebVTT: ${error.message}`);
    throw error;
  }
}

// Example usage
const sourceLanguage = "FR"; // Replace with the actual source language code
const targetLanguage = "ZH"; // Replace with the actual target language code
const inputFilePath = "D:/jason/projects/frpod/qplayer/assets/01-01.vtt"; // Replace with the actual input file path

getTranslatedVttForPathname(inputFilePath, targetLanguage, sourceLanguage)
  .then((translatedVtt) => {
    // Output the translated WebVTT
    console.log("Translated WebVTT:\n", translatedVtt);
  })
  .catch((error) => {
    console.error("Translation failed:", error);
  });
