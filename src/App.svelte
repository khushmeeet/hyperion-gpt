<script lang="ts">
  import { Configuration, OpenAIApi } from "openai";

  let configuration = new Configuration({
    apiKey: import.meta.env.VITE_OPENAI_API_KEY,
  });
  let openai = new OpenAIApi(configuration);

  let question = "";
  let answer = "";

  async function GPT3() {
    let response = await openai.createChatCompletion({
      model: "gpt-3.5-turbo",
      messages: [
        {
          role: "system",
          content:
            "You are an avid science fiction fan and have read Hyperion series by Dan Simmons four times. You have read all the books in Hyperion Catos series, which are Hyperion #1 and The Fall of Hyperion #2. Answer all the questions in detail and explain every concept in the given science fiction novels. DO NOT ANSWER QUESTION THAT IS NOT RELATED TO HYPERION CANTOS.",
        },
        { role: "user", content: question },
      ],
      temperature: 0.9,
      top_p: 1,
      frequency_penalty: 0,
      presence_penalty: 0,
      stream: false,
    });
    answer = response.data.choices[0].message.content;
  }
</script>

<main>
  <div class="header">
    <h1>Hyperion GPT</h1>
    <p>Ask questions on Hyperion Cantos Books.</p>
  </div>
  <div class="question">
    <form on:submit|preventDefault={GPT3}>
      <input type="text" bind:value={question} placeholder="Write a question" />
    </form>
  </div>
  <div class="answer">
    {#if answer != ""}
      <p>
        {answer}
      </p>
    {/if}
  </div>
</main>

<style lang="scss">
  @import url("https://fonts.googleapis.com/css2?family=Xanh+Mono&display=swap");
  @import url("https://fonts.googleapis.com/css2?family=Azeret+Mono&display=swap");
  :root {
    font-family: "Xanh Mono", monospace;
    font-weight: 400;
    background-color: rgba(255, 255, 255, 0.87);
    color: #242424;
    font-synthesis: none;
    text-rendering: optimizeLegibility;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    -webkit-text-size-adjust: 100%;
  }

  main {
    margin: 30px;
    padding: 20px;
  }

  .header {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 20px;

    h1 {
      font-size: 50px;
      font-weight: 700;
      margin: 0;
    }

    p {
      font-size: 20px;
    }
  }

  .question {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 20px;
    margin-left: 20%;
    margin-right: 20%;

    form {
      display: flex;
      flex-direction: column;
      align-items: center;
      width: 100%;

      input {
        width: 100%;
        padding: 10px;
        margin-bottom: 20px;
        font-size: 20px;
        border-radius: 3px;
        border: 0.125rem dashed #242424;
        background-color: rgba(255, 255, 255, 0.87);
        color: #242424;

        &:focus {
          outline: none;
        }
      }
    }
  }

  .answer {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 20px;

    p {
      text-align: justify;
      font-family: "Azeret Mono", monospace;
      font-size: 1.2rem;
      line-height: 1.7rem;
    }
  }
</style>
