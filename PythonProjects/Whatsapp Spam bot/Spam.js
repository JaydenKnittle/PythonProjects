let dataTransfer = new DataTransfer();
let box = document.querySelectorAll("[role=textbox]")[1];
if (!box) {
  alert("No chat open, Make sure you have opened the chat you want to spam.");
  throw new Error(
    "No chat open, Make sure you have opened the chat you want to spam."
  );
}

var count = prompt(
  "Enter number of messages:",
  "10"
);

  var message = prompt("MESSAGE YOU WANT TO SPAM : ", "Hello from spammer...");
  if (message == null || message == "") {
    alert("Please enter a message to spam. \nYou can re-run the script now.");
  } else {
    dataTransfer.setData("text/plain", message);

    (async () => {
      for (let i = 0; i < count; i++) {
      
        box.focus();
        box.dispatchEvent(
          new ClipboardEvent("paste", {
            clipboardData: dataTransfer,

            bubbles: true,
            cancelable: true,
            })
        ); 
        await new Promise((resolve) => setTimeout(resolve, 1000));
        box.parentElement.parentElement.parentElement.children[1].children[0].click();
        console.log(`"${message}" sent -> ${i + 1} times`);
      }
    })();
  }
