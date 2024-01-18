import { translate } from "deeplx";
const text = "hello world";
const sourceLanguage = "EN";
const targetLanguage = "FR"; // EN, FR, ZH
let result = await translate(text, targetLanguage, sourceLanguage);
console.log(`result = ${result}`);
