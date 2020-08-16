<template>
  <b-container fluid="lg">
    <b-row>
      <b-col sm="6">
        <b-form-input :type="url" v-model="msg" placeholder="URL"></b-form-input>
      </b-col>
      <b-col sm="2">
        <b-button
          type="submit"
          block
          variant="primary"
          v-bind:disabled="msg === ''"
          v-on:click="myfun"
        >Short</b-button>
      </b-col>
    </b-row>
    <b-row v-show="after">
      <b-col sm="6">
        <b-form-textarea plaintext :value="msg1"></b-form-textarea>
      </b-col>
      <b-col sm="2">
        <b-button type="reset" block variant="primary" v-on:click="reinit">Copy</b-button>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
export default {
  name: "HelloWorld",
  data() {
    return {
      msg: "",
      msg1: "",
      after: false
    };
  },
  methods: {
    reinit() {
      this.after = false;
      this.msg = "";
    },
    myfun() {
      this.axios
        .post("http://localhost:8000/shortener", {
          url: this.msg
        })
        // .then(response => console.log(response.data));
        .then(
          response => (this.msg1 = window.location.pathname + response.data.url)
        )
        .catch(error => {
          this.msg1 = error;
          this.after = true;
        })
        .finally(() => (this.after = true));
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
