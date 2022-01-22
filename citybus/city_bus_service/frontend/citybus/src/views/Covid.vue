<template >
    <div class="container">
    <div class="row">
        <div class="col-md-6 col-lg-6 my-3 center">
        <lottie-player src="https://assets10.lottiefiles.com/packages/lf20_3gmen1kz.json"  background="transparent"  speed="1"  style="width: 350px; height: 300px;"  loop  autoplay></lottie-player>
      </div>
      <div class="col-md-6 col-lg-6 my-5 ">
        <h1>Covid Safety guide</h1>
        <p>
            👉 Clean your hands often. <br>
            👉 Cough or sneeze in your bent elbow - not your hands! <br>
            👉 Avoid touching your eyes, nose and mouth.<br>
            👉 Avoid close contact with someone who is sick.<br>
            👉 Clean and disinfect frequently touched objects and surfaces.
        </p>
        
      </div>

      <!-- animation -->
      
    </div>
  </div>
</template>
<script>
export default {
    name:'Covid'
}
</script>
<style>
  .display-2{
  font-weight: 600;
}

.center{
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}

.form-label{
  font-weight: 900;
}
.display-4{
  font-weight: 400;
}  
</style>