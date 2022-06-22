import {
  app,
  get,
  App,
  post,
  redirect,
  contentType,
} from "https://denopkg.com/syumai/dinatra@0.15.0/mod.ts";
import { renderFile } from 'https://deno.land/x/dejs/mod.ts';

app(
  get('/', async () => new Response(await renderFile('index.ejs', { message: 'example' })))
);
