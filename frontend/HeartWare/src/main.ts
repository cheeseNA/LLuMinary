import "./assets/main.css";

import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";

/* import the fontawesome core */
import { library } from "@fortawesome/fontawesome-svg-core";

/* import font awesome icon component */
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

/* import specific icons */
import {
  faHippo,
  faGear,
  faTrash,
  faMusic,
  faPaperPlane,
} from "@fortawesome/free-solid-svg-icons";

/* add icons to the library */
library.add(faHippo);
library.add(faGear);
library.add(faTrash);
library.add(faMusic);
library.add(faPaperPlane);

const app = createApp(App).component("font-awesome-icon", FontAwesomeIcon);

app.use(router);

app.mount("#app");
