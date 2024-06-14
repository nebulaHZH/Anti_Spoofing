"use strict";(self["webpackChunkface_anti_front"]=self["webpackChunkface_anti_front"]||[]).push([[788],{8173:function(e,o,t){t.d(o,{hh:function(){return a}});t(4114);var i=t(6768),l={size:"1em",strokeWidth:4,strokeLinecap:"round",strokeLinejoin:"round",rtl:!1,theme:"outline",colors:{outline:{fill:"#333",background:"transparent"},filled:{fill:"#333",background:"#FFF"},twoTone:{fill:"#333",twoTone:"#2F88FF"},multiColor:{outStrokeColor:"#333",outFillColor:"#2F88FF",innerStrokeColor:"#FFF",innerFillColor:"#43CCF8"}},prefix:"i"};function n(){return"icon-"+(4294967296*(1+Math.random())|0).toString(16).substring(1)}function r(e,o,t){var i="string"===typeof o.fill?[o.fill]:o.fill||[],l=[],n=o.theme||t.theme;switch(n){case"outline":l.push("string"===typeof i[0]?i[0]:"currentColor"),l.push("none"),l.push("string"===typeof i[0]?i[0]:"currentColor"),l.push("none");break;case"filled":l.push("string"===typeof i[0]?i[0]:"currentColor"),l.push("string"===typeof i[0]?i[0]:"currentColor"),l.push("#FFF"),l.push("#FFF");break;case"two-tone":l.push("string"===typeof i[0]?i[0]:"currentColor"),l.push("string"===typeof i[1]?i[1]:t.colors.twoTone.twoTone),l.push("string"===typeof i[0]?i[0]:"currentColor"),l.push("string"===typeof i[1]?i[1]:t.colors.twoTone.twoTone);break;case"multi-color":l.push("string"===typeof i[0]?i[0]:"currentColor"),l.push("string"===typeof i[1]?i[1]:t.colors.multiColor.outFillColor),l.push("string"===typeof i[2]?i[2]:t.colors.multiColor.innerStrokeColor),l.push("string"===typeof i[3]?i[3]:t.colors.multiColor.innerFillColor);break}return{size:o.size||t.size,strokeWidth:o.strokeWidth||t.strokeWidth,strokeLinecap:o.strokeLinecap||t.strokeLinecap,strokeLinejoin:o.strokeLinejoin||t.strokeLinejoin,colors:l,id:e}}var s=Symbol("icon-context");function a(e,o,t){var a={name:"icon-"+e,props:["size","strokeWidth","strokeLinecap","strokeLinejoin","theme","fill","spin"],setup:function(a){var u=n(),c=(0,i.WQ)(s,l);return function(){var l=a.size,n=a.strokeWidth,s=a.strokeLinecap,p=a.strokeLinejoin,k=a.theme,d=a.fill,h=a.spin,f=r(u,{size:l,strokeWidth:n,strokeLinecap:s,strokeLinejoin:p,theme:k,fill:d},c),v=[c.prefix+"-icon"];return v.push(c.prefix+"-icon-"+e),o&&c.rtl&&v.push(c.prefix+"-icon-rtl"),h&&v.push(c.prefix+"-icon-spin"),(0,i.bF)("span",{class:v.join(" ")},[t(f)])}}};return a}},1788:function(e,o,t){t.r(o),t.d(o,{default:function(){return S}});var i=t(6768),l=t(144),n=t(4232),r=t(7477),s=t(8173),a=(0,s.hh)("upload-one",!0,(function(e){return(0,i.bF)("svg",{width:e.size,height:e.size,viewBox:"0 0 48 48",fill:"none"},[(0,i.bF)("path",{d:"M11.6777 20.271C7.27476 21.3181 4 25.2766 4 30C4 35.5228 8.47715 40 14 40C14.9474 40 15.864 39.8683 16.7325 39.6221",stroke:e.colors[0],"stroke-width":e.strokeWidth,"stroke-linecap":e.strokeLinecap,"stroke-linejoin":e.strokeLinejoin},null),(0,i.bF)("path",{d:"M36.0547 20.271C40.4577 21.3181 43.7324 25.2766 43.7324 30C43.7324 35.5228 39.2553 40 33.7324 40C32.785 40 31.8684 39.8683 30.9999 39.6221",stroke:e.colors[0],"stroke-width":e.strokeWidth,"stroke-linecap":e.strokeLinecap,"stroke-linejoin":e.strokeLinejoin},null),(0,i.bF)("path",{d:"M36 20C36 13.3726 30.6274 8 24 8C17.3726 8 12 13.3726 12 20",stroke:e.colors[0],"stroke-width":e.strokeWidth,"stroke-linecap":e.strokeLinecap,"stroke-linejoin":e.strokeLinejoin},null),(0,i.bF)("path",{d:"M17.0654 27.8812L23.9999 20.9238L31.1318 28.0002",stroke:e.colors[0],"stroke-width":e.strokeWidth,"stroke-linecap":e.strokeLinecap,"stroke-linejoin":e.strokeLinejoin},null),(0,i.bF)("path",{d:"M24 38.0001V24.4619",stroke:e.colors[0],"stroke-width":e.strokeWidth,"stroke-linecap":e.strokeLinecap,"stroke-linejoin":e.strokeLinejoin},null)])})),u=t(7796);const c=e=>((0,i.Qi)("data-v-7934e4ea"),e=e(),(0,i.jt)(),e),p={style:{display:"flex"}},k={class:"left_box"},d=c((()=>(0,i.Lk)("h2",{style:{display:"inline","margin-left":"10px"}},"图片上传",-1))),h=c((()=>(0,i.Lk)("br",null,null,-1))),f={class:"load_in"},v=c((()=>(0,i.Lk)("h5",{class:"tip"},"说明：上传成功后，点击图片分析即可查看分析结果",-1))),m={key:0},F={key:1,class:"load_out"},L={class:"right_box"},g=c((()=>(0,i.Lk)("h2",{style:{display:"inline","margin-left":"10px"}},"视频上传",-1))),b=c((()=>(0,i.Lk)("h5",{class:"tip"},"说明：要求尺寸最好是小于1GB格式为MP4",-1))),C={class:"load_in"},y=c((()=>(0,i.Lk)("br",null,null,-1))),_=c((()=>(0,i.Lk)("h5",{class:"tip"},"说明：上传成功后，点击视频分析即可查看分析结果",-1))),w={key:0,class:"load_out"},j=c((()=>(0,i.Lk)("span",null,"请等待...",-1))),W={key:1,class:"load_out"},x={controls:"",autoplay:"",width:"100%",class:"video",name:"media"},z=["src"];var R=(0,i.pM)({__name:"load",setup(e){const o=(0,l.KR)(""),t=(0,l.KR)(""),s=(0,l.KR)({name:"",url:""}),c=(0,l.KR)({name:"",url:""}),R=(0,l.KR)({email:localStorage.getItem("email")});function M(){alert("一次只能上传一张图片进行分析")}function Q(e){alert("上传成功"),console.log(e),s.value.url="/api"+e.url,s.value.name=e.filename,console.log(s.value)}function S(e){alert("上传成功"),console.log(e),c.value.url="/api"+e.url,c.value.name=e.filename,console.log(c.value)}function T(){alert("上传失败")}function E(){u.A.post("/analysis_picture",{email:R.value.email,filename:s.value.name}).then((e=>{console.log(e),o.value="/api"+e.image_path}))}function K(){u.A.post("/analysis_video",{email:R.value.email,filename:c.value.name}).then((e=>{console.log(e),t.value="/api"+e.video_path}))}return(e,u)=>{const c=(0,i.g2)("el-icon"),X=(0,i.g2)("el-upload"),A=(0,i.g2)("el-button"),q=(0,i.g2)("el-image"),B=(0,i.g2)("Loading");return(0,i.uX)(),(0,i.CE)("div",p,[(0,i.Lk)("div",k,[(0,i.Lk)("div",null,[(0,i.bF)((0,l.R1)(a),{style:{"vertical-align":"bottom"},theme:"filled",size:"30",fill:"#030000",strokeWidth:2,strokeLinecap:"square"}),d]),h,(0,i.Lk)("div",f,[(0,i.bF)(X,{class:"avatar-uploader",action:"/api/uploadimg",limit:1,"on-exceed":M,"on-success":Q,"on-error":T,data:R.value},{default:(0,i.k6)((()=>[(0,i.bF)(c,{class:"avatar-uploader-icon"},{default:(0,i.k6)((()=>[(0,i.bF)((0,l.R1)(r.FWt))])),_:1})])),_:1},8,["data"]),(0,i.bF)(A,{type:"primary",class:"submit_picture",onClick:E},{default:(0,i.k6)((()=>[(0,i.eW)(" 图片分析")])),_:1})]),v,""!==o.value?((0,i.uX)(),(0,i.CE)("h5",m,(0,n.v_)("analysis_"+s.value.name),1)):(0,i.Q3)("",!0),""!==o.value?((0,i.uX)(),(0,i.CE)("div",F,[(0,i.bF)(q,{class:"picture",src:o.value,"preview-src-list":[o.value],"preview-teleported":""},null,8,["src","preview-src-list"])])):(0,i.Q3)("",!0)]),(0,i.Lk)("div",L,[(0,i.Lk)("div",null,[(0,i.bF)((0,l.R1)(a),{style:{"vertical-align":"bottom"},theme:"filled",size:"30",fill:"#030000",strokeWidth:2,strokeLinecap:"square"}),g]),b,(0,i.Lk)("div",C,[(0,i.bF)(X,{class:"avatar-uploader",action:"/api/upload_video",limit:1,"on-exceed":M,"on-success":S,"on-error":T,data:R.value},{default:(0,i.k6)((()=>[(0,i.bF)(c,{class:"avatar-uploader-icon"},{default:(0,i.k6)((()=>[(0,i.bF)((0,l.R1)(r.FWt))])),_:1})])),_:1},8,["data"]),(0,i.bF)(A,{type:"primary",class:"submit_picture",onClick:K},{default:(0,i.k6)((()=>[(0,i.eW)(" 视频分析")])),_:1})]),y,_,""==t.value?((0,i.uX)(),(0,i.CE)("div",w,[j,(0,i.bF)(c,null,{default:(0,i.k6)((()=>[(0,i.bF)(B)])),_:1})])):(0,i.Q3)("",!0),""!==t.value?((0,i.uX)(),(0,i.CE)("div",W,[(0,i.Lk)("video",x,[(0,i.Lk)("source",{src:t.value,type:"video/mp4"},null,8,z)])])):(0,i.Q3)("",!0)])])}}}),M=t(1241);const Q=(0,M.A)(R,[["__scopeId","data-v-7934e4ea"]]);var S=Q}}]);
//# sourceMappingURL=788.9139ee56.js.map