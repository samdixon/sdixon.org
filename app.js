const { cwd, stdout, copy } = Deno;
import { serve } from "https://deno.land/x/sift@0.5.0/mod.ts";
import * as eta from "https://deno.land/x/eta@v1.12.3/mod.ts"

const templateDir = `${Deno.cwd()}/templates`;

for await (const dirEntry of Deno.readDir(templateDir)) {
  console.log(dirEntry);
}

async function renderTemplate(path) {
  return new Response(await eta.renderFile(`${templateDir}/${path}`), {
    headers: {
      'content-type': 'text/html'
    }
  })
}

serve({
  "/": () => renderTemplate('index.ejs'),
  "/projects": () => renderTemplate('projects.ejs'),
  "/about": () => renderTemplate('about.ejs'),
  "/blog": () => renderTemplate('blog.ejs'),
  "/blog/:slug": (_req, _conn, params) => {
    const post = `Hello, you visited ${params.slug}!`;
    return new Response(post);
  },
  // The route handler of 404 will be invoked when a route handler
  // for the requested path is not found.
  404: () => new Response("not found"),
});